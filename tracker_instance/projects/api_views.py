from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from tracker_instance.projects.serializers import ProjectSerializer
from tracker_instance.models import Project


class ProjectsList(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
