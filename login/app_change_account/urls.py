from django.urls import path
from . import views

urlpatterns = [
    path('', views.changeMe, name='changeMe')
]