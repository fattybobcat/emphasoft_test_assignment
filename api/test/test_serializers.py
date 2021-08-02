import pytest
from api.serializers import ReadOnlyUserSerializer

pytestmark = pytest.mark.django_db


def test_ReadOnlyUserSerializer_serializer_valid():
    data = {
            'id': 1,
            'username': 'test_user3',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'last_login': None,
            'is_active': False,
            'is_superuser': False,
     }
    serrializer = ReadOnlyUserSerializer(data=data)

    assert serrializer.is_valid()
    assert serrializer.errors == {}


def test_ReadOnlyUserSerializer_serializer_fail():
    data = {}
    serrializer = ReadOnlyUserSerializer(data=data)

    assert not serrializer.is_valid()


def test_WriteOnlyUserSerializer_serializer_valid():
    data = {
            'username': 'test_user3',
            'password': 'F4kePaSs0d',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'is_active': False,
     }
    serrializer = ReadOnlyUserSerializer(data=data)

    assert serrializer.is_valid()
    assert serrializer.errors == {}


def test_WriteOnlyUserSerializer_serializer_fail():
    data = {}
    serrializer = ReadOnlyUserSerializer(data=data)

    assert not serrializer.is_valid()
