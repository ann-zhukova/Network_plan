from django.shortcuts import render
from django.contrib.auth.models import Group
from .models import Worker, Department
from rest_framework import permissions, viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def manager_required_group(user):
    return user.groups.filter(name='Manager').exists()

@login_required(login_url='login')
def index(request):
    return render(request, 'account/main_projects.html')


@login_required(login_url='login')
def test(request):
    return render(request, 'account/network_graph.html')


@login_required(login_url='login')
def gantt(request):
    return render(request, 'account/gantt.html')

@login_required(login_url='/login/')
@user_passes_test(manager_required_group, login_url='account_index')
def departments(request):
    worker = request.user
    departments = list(Department.objects.all().values())
    return render(request, 'account/departments.html', {"departments": departments})


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        position = request.POST['position']
        about_user = request.POST['about_user']
        user_image = request.POST['user_image']
        worker = request.user
        worker.first_name = first_name
        worker.last_name = last_name
        worker.email = email
        worker.position = position
        worker.about_user = about_user
        worker.user_image = user_image
        worker.save()
    return render(request, 'account/profile.html')
