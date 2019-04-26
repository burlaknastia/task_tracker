from django.urls import path

from tracker_instance.projects.api_views import ProjectsList

urlpatterns = [
    path('', ProjectsList.as_view(), name='api-projects-list'),
]