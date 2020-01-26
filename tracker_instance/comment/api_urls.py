from django.urls import path

from tracker_instance.comment.api_views import CommentsList

urlpatterns = [
    path('', CommentsList.as_view(), name='api-comments-list'),
    # path('<int:id>/', TaskDetail.as_view(), name='api-task-detail'),
]
