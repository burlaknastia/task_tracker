from django.urls import path

from tracker_instance.project.api_views import ProjectsList

urlpatterns = [
    path('', ProjectsList.as_view(), name='api-projects-list'),
]
