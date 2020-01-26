from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response

from django_comments.models import Comment
from tracker_instance.comment.serializers import CommentsSerializer
from tracker_instance.models import Task, User
from tracker_instance.task.serializers import TaskSerializer, TaskDetailSerializer


class TasksList(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('status', 'project', 'owner', 'assignee')
    search_fields = ('title','descriptions__content')


class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    lookup_field = 'id'

    def patch(self, request, id, *args, **kwargs):
        payload = request.data
        instance = Task.objects.get(id=id)
        new_status = payload.get('status')
        new_assignee = payload.get('assignee')
        if new_assignee is not None:
            instance.assignee = User.objects.get(id=new_assignee)
        if new_status is not None:
            instance.status = new_status
        instance.save()
        serialized = self.serializer_class(instance, partial=True)
        return Response(serialized.data, status=status.HTTP_201_CREATED)


class TaskCommentsList(ListAPIView):
    serializer_class = CommentsSerializer
    lookup_field = 'id'

    def get_queryset(self):
        task_id = self.kwargs.get(self.lookup_field)
        task_comments = Comment.objects.filter(object_pk=task_id)
        return task_comments