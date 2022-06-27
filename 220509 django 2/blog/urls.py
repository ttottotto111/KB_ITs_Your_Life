from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_main, name='main'),
    path('list/', views.blog_list, name='list'),
    path('create/', views.blog_create ,name='create'),
    path('update/<int:pk>', views.blog_update, name='update'),
    path('delete/<int:pk>', views.blog_delete, name='delete'),
]
