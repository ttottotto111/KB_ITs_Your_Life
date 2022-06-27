from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index),
    path('calc_ui', views.calc_ui),
    path('calc_action', views.calc_action)
]