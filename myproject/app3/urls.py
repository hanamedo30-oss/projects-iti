from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_app3, name='home_app3'),
    path('update/<int:item_id>/', views.update_item_app3, name='update_item_app3'),
    path('delete/<int:item_id>/', views.delete_item_app3, name='delete_item_app3'),
]