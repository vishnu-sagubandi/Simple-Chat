from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='chat-home'),
    path('<str:room_name>/', views.room, name='room'),
]
