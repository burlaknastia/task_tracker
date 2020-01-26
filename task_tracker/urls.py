from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tracker_instance.task.api_urls')),
    path('api/descriptions/', include('tracker_instance.description.api_urls')),
    path('api/comments/', include('tracker_instance.comment.api_urls')),
    path('api/projects/', include('tracker_instance.project.api_urls')),
]
