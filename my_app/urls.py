from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    path('depart/<int:nid>/edit/', views.depart_edit),
    path('employee/list/', views.employee_list),
    path('employee/add/', views.employee_add),
    path('employee/<int:nid>/edit/', views.employee_edit),
    path('employee/<int:nid>/delete/', views.employee_delete),
    path('admin/list/', views.admin_list),
    path('admin/add/', views.admin_add),
    path('admin/<int:nid>/edit/', views.admin_edit),
    path('admin/<int:nid>/delete/', views.admin_delete),
    path('', views.login, name='login'),
    path('logout/', views.logout),
]