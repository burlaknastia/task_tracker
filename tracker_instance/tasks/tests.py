import json

from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django_comments.models import Comment
from rest_framework.test import APIClient

from tracker_instance.models import Project, Task
from task_tracker.settings import SITE_ID


class TasksAPITestCase(TestCase):
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

    def test_create_task(self):
        project_id = self.project.id
        user_id = self.user.id
        res = self.c.post('/api/tasks/',
                          {"title": "test_task_new",
                           "status": "open",
                           "project": project_id,
                           "owner": user_id,
                           "assignee": user_id,
                           "descriptions": [{"content": "test_content"},
                                            {"content": "another test content"}]}
                          , format='json')
        self.assertEqual(res.status_code, 201)

    def test_patch_task(self):
        api_url = f'/api/tasks/{self.task.id}/'
        res = self.c.patch(api_url, {"status": "done"}, format='json')
        self.assertEqual(res.status_code, 201)

    def test_delete_task(self):
        api_url = f'/api/tasks/{self.task.id}/'
        res = self.c.delete(api_url)
        self.assertEqual(res.status_code, 204)

    def test_get_tasks(self):
        res = self.c.get('/api/tasks/')
        self.assertEqual(res.status_code, 200)
        res = self.c.get('/api/tasks/?status=open&project=&owner=&assignee=')
        res_json = json.loads(res.content)
        self.assertEqual(len(res_json), 1)
        res = self.c.get('/api/tasks/?status=in_progress&project=&owner=&assignee=')
        res_json = json.loads(res.content)
        self.assertEqual(len(res_json), 0)

    def test_get_task_info(self):
        task_id = str(self.task.id)
        api_url = f'/api/tasks/{self.task.id}/'
        res = self.c.get(api_url)
        res_json = json.loads(res.content)
        self.assertEqual(res_json['comments_count'], 0)
        self.assertEqual(res_json['users_commented_count'], 0)
        site = Site.objects.get(id=SITE_ID)
        ct = ContentType.objects.get_for_model(Task)
        comment = Comment.objects.create(comment="task comment test",
                                         user=self.user,
                                         content_type=ct,
                                         object_pk=task_id,
                                         site=site)
        res = self.c.get(api_url)
        res_json = json.loads(res.content)
        self.assertEqual(res_json['comments_count'], 1)
        self.assertEqual(res_json['users_commented_count'], 1)

        another_comment = Comment.objects.create(comment="another task comment test",
                                                 user=self.user,
                                                 content_type=ct,
                                                 object_pk=task_id,
                                                 site=site)
        res = self.c.get(api_url)
        res_json = json.loads(res.content)
        self.assertEqual(res_json['comments_count'], 2)
        self.assertEqual(res_json['users_commented_count'], 1)
