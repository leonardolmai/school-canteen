from django.urls import path
from . import views

urlpatterns = [
    path('', views.SaleList.as_view(), name='sales'),
    path('register-sale/', views.RegisterSale.as_view(), name='register-sale'),
    path('detail/<int:pk>', views.SaleDetail.as_view(), name='detail_sale'),
    path('day-report/', views.DayReport.as_view(), name='day-report'),
    path('week-report/', views.WeekReport.as_view(), name='week-report'),
    path('month-report/', views.MonthReport.as_view(), name='month-report'),
]
