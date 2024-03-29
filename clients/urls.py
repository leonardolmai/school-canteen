from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientList.as_view(), name='clients'),
    path('add/', views.ClientCreate.as_view(), name='add_client'),
    path('detail/<int:pk>/', views.ClientDetail.as_view(), name='detail_client'),
    path('edit/<int:pk>/', views.ClientUpdate.as_view(), name='edit_client'),
    path('delete/<int:pk>/', views.ClientDelete.as_view(), name='delete_client'),
]
