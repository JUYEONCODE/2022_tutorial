from tkinter import INSERT
from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('insert/', views.insert),
]