from django.urls import path

from tracker_instance.task.api_views import TasksList, TaskDetail, \
    TaskCommentsList

urlpatterns = [
    path('', TasksList.as_view(), name='api-tasks-list'),
    path('<int:id>/', TaskDetail.as_view(), name='api-task-detail'),
    path('<int:id>/comments/', TaskCommentsList.as_view(), name='api-task-comments'),
]