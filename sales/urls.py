from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales, name='sales'),
    path('add-cart-product/<int:id>', views.add_cart_product, name='add-cart-product'),
    path('delete-cart-product/<int:id>', views.delete_cart_product, name='delete-cart-product'),
    path('register-sale/', views.register_sale, name='register-sale'),
    path('day-report/', views.day_report, name='day-report'),
    path('week-report/', views.week_report, name='week-report'),
    path('month-report/', views.month_report, name='month-report'),
]
