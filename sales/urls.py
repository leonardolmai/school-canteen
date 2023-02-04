from django.urls import path
from . import views

urlpatterns = [
    path('', views.SaleList.as_view(), name='sales'),
    path('register-sale/', views.RegisterSale.as_view(), name='register-sale'),
    path('detail/<int:pk>', views.SaleDetail.as_view(), name='detail_sale'),
    path('day-report/', views.day_report, name='day-report'),
    path('week-report/', views.week_report, name='week-report'),
    path('month-report/', views.month_report, name='month-report'),
]
