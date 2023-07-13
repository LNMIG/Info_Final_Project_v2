from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.post, name='posts'),
    path('developers/', views.developers, name='developers'),
]