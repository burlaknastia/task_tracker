from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django_comments.models import Comment

OPEN = "open"
IN_PROGRESS = "in_progress"
DONE = "done"

TASK_STATUS_CHOICES = (
    (OPEN, "Открыт"),
    (IN_PROGRESS, "В работе"),
    (DONE, "Завершен")
)


class User(AbstractUser):
    pass


class Description(models.Model):
    content = models.TextField()
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='descriptions')


class Task(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES,
                              default=OPEN, null=False)
    project = models.ForeignKey('Project', on_delete=models.CASCADE,
                                related_name='tasks', null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='owner_tasks', default=1, null=False)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', default=1)
    comments = GenericRelation(Comment, object_id_field='object_pk', related_query_name='tasks')

    def __str__(self):
        return f'{self.title}: {self.status}'

    class Meta:
        unique_together = ('title', 'project')


class Project(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
