from django.urls import path, include
from account import views
from django.contrib.auth import views as auth_views
from . import test
from . import gantt

urlpatterns = [
    path('', views.index, name='account_index'),
    path('networkGraph', views.test, name='networkGraph'),
    path('gantt', views.gantt, name='gantt'),
    path('departments', views.departments, name='departments'),
    path('profile', views.profile, name='profile')
]