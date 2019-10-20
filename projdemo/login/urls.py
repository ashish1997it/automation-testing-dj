from django.urls import path, include
from rest_framework import routers
from django.conf.urls import include, url
from .api.v1.login_view import LoginView


urlpatterns = [
    # API
    path('api/v1/login-user/', LoginView.user_login, name='user-login'),
    path('api/v1/logout/', LoginView.user_logout, name='user-logout'),
    path('api/v1/get-message/', LoginView.get_message, name='get-message'),
]
