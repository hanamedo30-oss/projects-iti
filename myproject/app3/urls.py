from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_app3, name='home_app3'),
]