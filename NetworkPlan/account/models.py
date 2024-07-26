from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Department(models.Model):
    """Подразделение"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()

    # Метаданные
    class Meta:
        ordering = ['-name']

    # Methods
    def __str__(self):
        """Строка для представления объекта MyModelName (например, в административной панели и т.д.)."""
        return 'department_' + self.name


class Worker(AbstractUser):
    """пользователь"""

    # Поля
    about_user = models.CharField(max_length=200)
    user_image = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    department = models.ForeignKey(
        Department,
        null=True,
        on_delete=models.CASCADE)

    # Метаданные
    class Meta:
        ordering = ['-username']

    # Methods
    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к определенному экземпляру MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return str(self.username)


class Project(models.Model):
    """Проект"""

    # Поля
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text='Введите название проекта')
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()  # дата начала работы
    end_date = models.DateField(blank=True, null=True)  # дата начала работы

    # Метаданные
    class Meta:
        ordering = ['-id']

    # Methods
    def __str__(self):
        """Строка для представления объекта MyModelName (например, в административной панели и т.д.)."""
        return 'project_' + self.name


class Stage(models.Model):
    """Этап"""
    # Поля
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text='Введите название проекта')
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()  # дата начала работы
    end_date = models.DateField(blank=True, null=True)  # дата начала работы
    status = models.CharField(max_length=20)  # готова - в процессе - не начата
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )

    # Метаданные
    class Meta:
        ordering = ['-id']

    # Methods
    def __str__(self):
        """Строка для представления объекта MyModelName (например, в административной панели и т.д.)."""
        return 'stage_' + self.name


class Task(models.Model):
    """Задачи в проекте """

    # Поля
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text='Задача')
    description = models.TextField(help_text='Описание задачи', blank=True, null=True)
    start_date = models.DateField()  # дата начала работы
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100)  # готова - в процессе - не начата
    stage = models.ForeignKey(
        Stage,
        on_delete=models.CASCADE,
    )

    # Метаданные
    class Meta:
        ordering = ['-id']

    # Methods
    def __str__(self):
        """Строка для представления объекта MyModelName (например, в административной панели и т.д.)."""
        return 'task_' + self.name


class UserDoTask(models.Model):
    """Задачи в проекте """

    # Поля
    worker = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
    )

    # Метаданные
    class Meta:
        unique_together = ['worker', 'task']
        ordering = ['worker', 'task']

    # Methods
    def __str__(self):
        """Строка для представления объекта MyModelName (например, в административной панели и т.д.)."""
        return str(self.worker) + '_do_' + str(self.task)


class Resource(models.Model):
    """Ресурсы"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text='Задача')
    description = models.TextField(help_text='Описание задачи', blank=True, null=True)
    type = models.CharField(max_length=100, help_text='Задача', blank=True, null=True)  # дата начала работы
    is_working = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    # Methods
    def __str__(self):
        """Строка для представления объекта MyModelName (например, в административной панели и т.д.)."""
        return 'resource_' + self.name


class TaskUseResource(models.Model):
    """Задачи в проекте """

    # Поля
    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
    )

    # Метаданные
    class Meta:
        unique_together = ['resource', 'task']
        ordering = ['resource', 'task']

    # Methods
    def __str__(self):
        """Строка для представления объекта MyModelName (например, в административной панели и т.д.)."""
        return str(self.resource) + '_used_in_' + str(self.task)
