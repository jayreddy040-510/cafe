from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('users/', views.getUsers, name="users"),
    path('users/<str:id>', views.getUser, name="user")
]