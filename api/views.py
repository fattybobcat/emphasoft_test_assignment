import requests
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import ReadOnlyUserSerializer, WriteOnlyUserSerializer


class UsersViewSet(APIView):

    def get(self, request: requests.Request) -> Response:
        users = User.objects.all()
        serializer = ReadOnlyUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request: requests.Request) -> Response:
        serializer = WriteOnlyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserIdViewSet(APIView):

    def get(self, request: requests.Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        if user:
            serializer = ReadOnlyUserSerializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: requests.Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        serializer = WriteOnlyUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: requests.Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        serializer = WriteOnlyUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: requests.Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        if user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
