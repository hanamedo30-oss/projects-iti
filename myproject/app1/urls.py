from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_app1, name='home_app1'),
    path('update/<int:item_id>/', views.update_item_app1, name='update_item_app1'),
    path('delete/<int:item_id>/', views.delete_item_app1, name='delete_item_app1'),
]