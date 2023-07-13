from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.post, name='posts'),
]