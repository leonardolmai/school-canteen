from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='products'),
    path('add/', views.ProductCreate.as_view(), name='add_product'),
    path('detail/<int:pk>', views.ProductDetail.as_view(), name='detail_product'),
    path('edit/<int:pk>/', views.ProductUpdate.as_view(), name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
]
