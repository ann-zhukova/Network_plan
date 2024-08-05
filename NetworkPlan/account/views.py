from django.db.models import F
import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.urls import reverse

from .models import Worker, Department, Project, UserDoTask, Stage, Task
from rest_framework import permissions, viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def manager_required_group(user):
    return user.groups.filter(name='Manager').exists()


@login_required(login_url='login')
def index(request):
    worker = request.user
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        project = Project.objects.create(name=name, description=description, start_date=datetime.date.today())
        project.save()
        stage = Stage.objects.create(name='создание', project=project, start_date=datetime.date.today())
        stage.save()
        task = Task.objects.create(name="coздание проекта", stage=stage, start_date=datetime.date.today())
        task.save()
        userdotask = UserDoTask.objects.create(worker=worker, task=task)
        userdotask.save()
        return redirect(reverse('account_index'))
    else:
        projects = list(
            UserDoTask.objects.
            select_related('task').filter(worker=worker).
            select_related('task__stage').
            select_related('task__stage__project').
            values(
                project_id=F('task__stage__project_id'),
                name=F('task__stage__project__name'),
                description=F('task__stage__project__description'),
                start_date=F('task__stage__project__start_date'),
                end_date=F('task__stage__project__end_date')),
            )
    # projects_db = (UserDoTask.objects.
    #                select_related('task').
    #                filter(worker=worker).
    #                prefetch_related('task__stage').
    #                select_related('task__stage__project').
    #                all())
    #
    # projects = []
    # for project in projects_db:
    #     projects.append({'project_id': project.task__stage__project.id,
    #                      'name': project.task__stage__project.name,
    #                      'description': project.task__stage__project.description,
    #                      'start_date': project.task__stage__project.start_date,
    #                      'end_date': project.task__stage__project.end_date,
    #                      'stages': [stage.name for stage in project.task__stage]
    #                      })
    # projects = list(Project.objects.all().values())
        return render(request, 'account/main_projects.html', {"projects": projects})


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


@login_required(login_url='/login/')
def stages(request, object_id):
    project_id = object_id
    stages = list(Stage.objects.filter(project_id=project_id).values())
    return render(request, 'account/stages.html', {"stages": stages})
    #return HttpResponse(f"You are viewing object with ID: {stages[0]['name']}")


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

from django.core.mail import send_mail

@login_required(login_url='login')
def send_email(request):
    if request.method == 'POST':
        password = Worker.objects.make_random_password(length=8)
    # Ваш код для получения имени аккаунта и пароля пользователя
        new_user = Worker.objects.create_user(
        username='2',
        email='-',
        password=password)
        new_user.save()
    # Затем используйте функцию send_mail для отправки письма
        send_mail(
            'Вас пригласили',
            f'Это тестовое письмо  '
            f'Имя пользователя: {new_user.username}, '
            f'Пароль: {password}',
            '-',
            [new_user.email],
            fail_silently=False,
         )
        return HttpResponse("письмо отправлено")
    else:
        return HttpResponse("запрещен доступ")
