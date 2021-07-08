from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.student_list,name = 'student_list'),
    path('view/<int:pk>', views.detailed_view,name = 'detailed_view'),
    path('update/<int:pk>', views.update_view,name = 'edit_update'),
    path('delete/<int:pk>', views.delete,name = 'delete'),
    path('create/', views.create,name = 'create'),





]