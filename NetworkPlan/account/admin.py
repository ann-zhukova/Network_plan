from django.contrib import admin
from .models import Worker, Department, Stage, Project, Task, UserDoTask, Resource, TaskUseResource
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm


# Register your models here.

# from .models import Post
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Worker
    list_display = ['email', 'username', 'position', 'about_user', 'department']


admin.site.register(Worker, CustomUserAdmin)

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Department)
admin.site.register(Stage)
admin.site.register(UserDoTask)
admin.site.register(Resource)
admin.site.register(TaskUseResource)
