from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    def handle(self, *args, **options):
        manager = Group(name='Manager')  # Начальник проекта
        planner = Group(name='Planner')  # Планировщики
        executor = Group(name='Executor')  # Исполнители
        manager.save()
        planner.save()
        executor.save()

        # Разрешения
        create_project = Permission.objects.create(
            codename='create_project',
            name='Создание проекта'
        )
        create_project.save()
        create_stage = Permission.objects.create(
            codename='create_stage',
            name='Создание этапа'
        )
        create_stage.save()
        create_task = Permission.objects.create(
            codename='create_task',
            name='Создание задачи'
        )
        manager.permissions.add(create_project)
        manager.permissions.add(create_stage)
        manager.permissions.add(create_task)
        planner.permissions.add(create_stage)
        planner.permissions.add(create_task)
