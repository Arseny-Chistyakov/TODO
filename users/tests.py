from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase

from users.models import User
from users.views import CustomUserViewSet


class TestCustomUserViewSetTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.url = '/api/users/'
        self.format = 'json'
        self.user = User.objects.create(username='bibo', first_name='asd', last_name='sdvds', email='sa@mail.ru')
        self.user_dict = {'username': 'oou', 'first_name': 'luyyfuy', 'last_name': 'guuyg', 'email': '002oo0@gmail.com'}
        self.admin = User.objects.create_superuser(username='admin', email='2@mail.ru', password='admin_wewf')

    def tearDown(self) -> None:
        pass

    def test_APIRequestFactory_list_not_auth(self):
        request = self.factory.get(self.url)
        view = CustomUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_APIClient_detail_not_auth(self):
        response = self.client.get(f'{self.url}{self.user.uid}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_APIClient_detail_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(f'{self.url}{self.user.uid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_APIClient_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(f'{self.url}{self.user.uid}/', self.user_dict, format=self.format)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, self.user_dict.get('first_name'))
        self.assertEqual(self.user.last_name, self.user_dict.get('last_name'))
        self.assertEqual(self.user.email, self.user_dict.get('email'))
        self.client.logout()


class TestCustomUserViewSetAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.url = '/api/users/'
        self.user_dict = {'username': 'oou', 'email': '002oo0@gmail.com'}
        self.admin = User.objects.create_superuser(username='admin', email='2@mail.ru', password='admin_wewf')

    def tearDown(self) -> None:
        pass

    def test_APITestCase_create_not_auth(self):
        response = self.client.post(self.url, data=self.user_dict)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_APITestCase_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(self.url, data=self.user_dict)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.client.logout()
