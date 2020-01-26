from django.db.models import Count
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from tracker_instance.description.serializers import DescriptionSerializer
from tracker_instance.models import Task, Description


class TaskSerializer(ModelSerializer):
    descriptions = DescriptionSerializer(many=True, partial=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'status', 'project', 'owner',
                  'assignee', 'descriptions')

    def create(self, validated_data):
        descriptions = validated_data.pop('descriptions')
        task = Task.objects.create(**validated_data)
        for desc in descriptions:
            if desc.get('content') is not None:
                Description.objects.create(content=desc['content'],
                                           task=task)
        return task


class TaskDetailSerializer(ModelSerializer):
    descriptions = DescriptionSerializer(many=True, partial=True)
    comments_count = IntegerField(source='comments.count', read_only=True)
    users_commented_count = SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'title', 'status', 'project', 'owner',
                  'assignee', 'descriptions', 'comments_count',
                  'users_commented_count')

    def get_users_commented_count(self, obj):
        count = Task.objects.values('id').annotate(
            user_count=Count('comments__user', distinct=True))\
            .filter(id=obj.id).first()
        return count['user_count']