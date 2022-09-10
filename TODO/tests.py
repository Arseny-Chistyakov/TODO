import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase

from users.models import User
from .models import Project, TODO
from .views import ProjectModelViewSet


class TestProjectModelViewSet(TestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.url = '/api/projects/'
        self.format = 'json'
        self.user = User.objects.create_user(username='riva', password='bhj5', email='12@mail.ru')
        self.admin = User.objects.create_superuser(username='admin', email='2@mail.ru', password='admin_woof')
        self.project_dict = {'name': 'm', 'repository': 'https://g.ru', 'creators_project': {self.user.username}}
        # т.к.поле сериализуется SlugRelatedField,без него было бы - {self.user.uid}
        self.project = Project.objects.create(name='test_project', repository='https://g.ru')
        self.project.save()
        self.project.creators_project.set([self.user])

    def tearDown(self) -> None:
        pass

    def test_APIRequestFactory_list_not_auth(self):
        view = ProjectModelViewSet.as_view({'get': 'list'})
        request = self.factory.get(self.url)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_APIRequestFactory_list_admin(self):
        view = ProjectModelViewSet.as_view({'get': 'list'})
        request = self.factory.get(self.url)
        force_authenticate(request, user=self.admin)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_APIClient_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(self.url, self.project_dict, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

    def test_APIClient_detail_not_auth(self):
        response = self.client.get(f'{self.url}{self.project.uid}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_APIClient_detail_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(f'{self.url}{self.project.uid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_APIClient_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(f'{self.url}{self.project.uid}/', {'name': 'edited'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, 'edited')
        self.client.logout()


class TestTodoViewSet(APITestCase):

    def setUp(self) -> None:
        self.url = '/api/TODOs/'
        self.user = User.objects.create_user(username='tiva', password='bhj5', email='1@mail.ru')
        self.admin = User.objects.create_superuser(username='admin0', email='2@mail.ru', password='admin_woof')
        self.project_dict = {'name': 'm3', 'repository': 'https://g.ru', 'creators_project': {self.user.username}}
        self.project = Project.objects.create(name='test_project', repository='https://g.ru')
        self.project.save()
        self.project.creators_project.set([self.user])
        self.TODO_dict = {'body': 'test_content', 'creator_keep': {self.user.username}, 'project': {self.project.name}}
        self.TODO = TODO.objects.create(body='fix', project=self.project, creator_keep=self.user,
                                        project_id=self.project.uid, creator_keep_id=self.user.uid)

    def test_APIClient_list_not_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_APIClient_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_APIClient_create_not_auth(self):
        response = self.client.post(self.url, data=self.TODO_dict)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_APIClient_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(self.url, data=self.TODO_dict)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

    def test_APIClient_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(f'{self.url}{self.TODO.uid}/', {
            'body': 'test_content_changed',
            'project': self.TODO.project.name,
            'creator_keep': self.TODO.creator_keep.username,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.TODO.refresh_from_db()
        self.assertEqual(json.loads(response.content)['body'], 'test_content_changed')
        self.client.logout()
