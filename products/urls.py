from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
]
