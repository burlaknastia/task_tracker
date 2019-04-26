from django.contrib import admin
from tracker_instance.models import Task, Description, Project, User

admin.site.register(Task)
admin.site.register(Description)
admin.site.register(Project)
admin.site.register(User)
