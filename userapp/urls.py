from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register',views.userreg),
    path('login',views.login),
    path('home',views.home),
    path('logout',views.logout),
    path('predic',views.predic),
]