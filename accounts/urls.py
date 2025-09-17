from django.urls import path
from rest_framework_simplejwt.views import (token_obtain_pair, token_refresh)
from .views import *

urlpatterns = [
    path('auth/token/', token_obtain_pair, name='token_obtain_pair'),
    path('auth/token/refresh/', token_refresh, name='token_refresh'),

    path('auth/register/', RegisterAPIView.as_view(), name='register'),
    path('users/', UsersListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UsersRetrieveUpdateDestroyAPIView.as_view(), name='user_detail'),
    path('me/', MyAccountAPIView.as_view(), name='my_account'),
]
