from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('check/',views.set),
    path('temp/',views.message)
]
