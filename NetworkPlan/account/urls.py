from django.urls import path, include
from account import views
from django.contrib.auth import views as auth_views
from . import test

urlpatterns = [
    path('', views.index, name='account_index'),
    path('networkGraph', views.test, name='networkGraph')
]