from django.urls import path
from . import views
from app_welcome import views as app_welcome_views

urlpatterns = [
    path('', views.loginMe, name="login"),
    path('', app_welcome_views.welcome, name="welcome"),
]