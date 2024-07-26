from django.shortcuts import render
from django.contrib.auth.models import Group
from .models import Worker
from rest_framework import permissions, viewsets
from django.contrib.auth.decorators import login_required
from .serializers import GroupSerializer, UserSerializer
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def manager_required_group(user):
    return user.groups.filter(name='Manager').exists()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Worker.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


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
    return render(request, 'account/departments.html')


@login_required(login_url='login')
def profile(request):
    return render(request, 'account/profile.html')
