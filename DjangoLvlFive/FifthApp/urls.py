from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from FifthApp import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('other/', views.other, name='other')
]
