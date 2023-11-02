
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

import authentication.views as authentication

app_name = 'authentication'

urlpatterns = [
    path('register/', authentication.UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', authentication.UsersList.as_view(), name='users-index'),
    path('users/<int:pk>/', authentication.UserDetailView.as_view(), name='user-detail')
]
