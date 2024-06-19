from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from account.models import Project, Task, Stage


class Command(BaseCommand):
    def handle(self, *args, **options):
        manager = Group(name='Manager')  # Начальник проекта
        planner = Group(name='Planner')  # Планировщики
        executor = Group(name='Executor')  # Исполнители
        manager.save()
        planner.save()
        executor.save()

        content_project = ContentType.objects.get_for_model(Project)
        content_task = ContentType.objects.get_for_model(Task)
        content_stage = ContentType.objects.get_for_model(Stage)
        # Разрешения
        create_project = Permission.objects.create(
            codename='create_project',
            name='Создание проекта',
            content_type=content_project
        )
        create_project.save()
        create_stage = Permission.objects.create(
            codename='create_stage',
            name='Создание этапа',
            content_type=content_stage
        )
        create_stage.save()
        create_task = Permission.objects.create(
            codename='create_task',
            name='Создание задачи',
            content_type=content_task
        )
        create_task.save()
        manager.permissions.add(create_project)
        manager.permissions.add(create_stage)
        manager.permissions.add(create_task)
        planner.permissions.add(create_stage)
        planner.permissions.add(create_task)
