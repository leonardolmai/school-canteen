from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients, name='clients'),
    path('add/', views.add_client, name='add_client'),
    path('edit/<int:id>/', views.edit_client, name='edit_client'),
    path('delete/<int:id>/', views.delete_client, name='delete_client'),
]
