from django.urls import path
from rest_framework_simplejwt.views import (token_obtain_pair, token_refresh)
from .views import *

urlpatterns = [
    path('token/', token_obtain_pair, name='token_obtain_pair'),
    path('token/refresh/', token_refresh, name='token_refresh'),

    path('api/register/', RegisterAPIView.as_view(), name='register'),
    path('api/users/', UsersListAPIView.as_view(), name='user_list'),
    path('api/users/<int:pk>/', UsersRetrieveUpdateDestroyAPIView.as_view(), name='user_detail'),
    path('api/me/', MyAccountView.as_view(), name='my_account'),
]
