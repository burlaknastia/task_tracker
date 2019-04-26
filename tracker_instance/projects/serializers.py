from rest_framework.serializers import ModelSerializer

from tracker_instance.models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title')
