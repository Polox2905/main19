from django.urls import path, include
from .views import post_list

urlpatterns = [
    path('posts/', post_list, name='post_list'),
]