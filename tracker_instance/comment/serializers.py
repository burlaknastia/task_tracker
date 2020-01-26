from django.contrib.contenttypes.models import ContentType
from django_comments.models import Comment
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer


class CommentsSerializer(ModelSerializer):
    content_type = SlugRelatedField(slug_field='model',
                                    queryset=ContentType.objects.all())

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'user',
                  'content_type', 'object_pk', 'site')
