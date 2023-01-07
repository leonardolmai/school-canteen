from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeList.as_view(), name='employees'),
    path('add/', views.EmployeeCreate.as_view(), name='add_employee'),
    path('detail/<int:pk>', views.EmployeeDetail.as_view(), name='detail_employee'),
    path('edit/<int:pk>/', views.EmployeeUpdate.as_view(), name='edit_employee'),
    path('delete/<int:pk>/', views.EmployeeDelete.as_view(), name='delete_employee'),
]
