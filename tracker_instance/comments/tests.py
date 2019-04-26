from django.contrib.auth import get_user_model
from django.test import TestCase
from django_comments.models import Comment
from rest_framework.test import APIClient

from tracker_instance.models import Project, Task


class CommentsAPITestCase(TestCase):
    c = APIClient()

    def setUp(self):
        get_user_model().objects.create_superuser('auto_test_user', '', 'password')
        self.c.login(username='auto_test_user', password='password')
        self.user = get_user_model().objects.get(username='auto_test_user')
        self.project = Project.objects.create(title='test_project')
        self.task = Task.objects.create(title='test_task',
                                        status='open',
                                        project=self.project,
                                        owner=self.user,
                                        assignee=self.user)

    def test_create_comment(self):
        task_id = str(self.task.id)
        res = self.c.post('/api/comments/',
                          {"comment": "task comment test",
                           "user": self.user.id,
                           "content_type": "task",
                           "object_pk": task_id }
                          , format='json')
        self.assertEqual(res.status_code, 201)