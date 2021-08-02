from django.urls import path

from . import views


urlpatterns = [
    path('v1/users/', views.UsersViewSet.as_view(), name="user-all"),
    path("v1/users/<int:user_id>/", views.UserIdViewSet.as_view(), name='user'),
]
