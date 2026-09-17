from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_app2, name='home_app2'),
    path('update/<int:item_id>/', views.update_item_app2, name='update_item_app2'),
    path('delete/<int:item_id>/', views.delete_item_app2, name='delete_item_app2'),
]