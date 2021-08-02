import pytest
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User


pytestmark = pytest.mark.django_db

client = APIClient


class RemoteAuthenticatedTest(APITestCase):

    def setUp(self):
        self.username = 'mister_neutron'
        self.user = User.objects.create_user(username='mister_neutron',
                                             password='F4kePaSs0d')
        Token.objects.create(user=self.user)
        super(RemoteAuthenticatedTest, self).setUp()
        User.objects.create(
            username='test_user_2',
            password='F4kePaSs0d',
            first_name='first_name',
            last_name='last_name',
            is_active=False,
            is_superuser=False,
        )

    @pytest.mark.django_db(transaction=True)
    def test_user_not_auth(self):
        url = '/api/v1/users/'
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @pytest.mark.django_db(transaction=True)
    def test_auth_user_get_info(self):
        url = '/api/v1/users/'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db(transaction=True)
    def test_auth_user_post_new_user_with_right_data(self):
        count_user = User.objects.all().count()
        url = '/api/v1/users/'
        data = {
            'username': 'test_user',
            'password': 'Abcd321.',
            'is_active': False,
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.all().count() == count_user + 1

    @pytest.mark.django_db(transaction=True)
    def test_auth_user_post_new_user_with_wrong_data(self):
        count_user = User.objects.all().count()
        url = '/api/v1/users/'
        data = {}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.post(url, data)
        print(response)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert User.objects.all().count() == count_user

    @pytest.mark.django_db(transaction=True)
    def test_auth_user_get_user_by_id(self):
        url = '/api/v1/users/1/'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db(transaction=True)
    def test_auth_user_patch_user_by_id(self):
        url = '/api/v1/users/1/'
        data = {
            'first_name': 'test_first_name'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.patch(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert response.json().get('id') == 1
        assert response.json().get('first_name') == 'test_first_name'

    @pytest.mark.django_db(transaction=True)
    def test_auth_user_put_user_by_id(self):
        url = '/api/v1/users/2/'
        data = {
            'username': 'put_user',
            'password': 'fattybobcatS1',
            'is_active': True,
            'first_name': 'test_first_name',
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.put(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json().get('id') == 2
        assert response.json().get('first_name') == 'test_first_name'
        assert response.json().get('username') == 'put_user'

    @pytest.mark.django_db(transaction=True)
    def test_auth_user_delete_user_by_id(self):
        url = '/api/v1/users/2/'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
