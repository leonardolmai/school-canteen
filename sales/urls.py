from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales, name='sales'),
    path('day-report/', views.day_report, name='day-report'),
    path('week-report/', views.week_report, name='week-report'),
    path('month-report/', views.month_report, name='month-report'),
]
