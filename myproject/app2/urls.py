from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_app2, name='home_app2'),
]