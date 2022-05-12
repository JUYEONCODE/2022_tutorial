from tkinter import INSERT
from django.urls import path
from secondapp import views

urlpatterns = [
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('army_shop/', views.army_shop),
]
