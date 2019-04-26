from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tracker_instance.tasks.api_urls')),
    path('api/descriptions/', include('tracker_instance.descriptions.api_urls')),
    path('api/comments/', include('tracker_instance.comments.api_urls')),
    path('api/projects/', include('tracker_instance.projects.api_urls')),
]
