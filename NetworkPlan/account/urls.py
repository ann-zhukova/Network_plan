from django.urls import path, include
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='account_index')
]