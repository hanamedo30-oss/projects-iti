from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_app1, name='home_app1'),
]