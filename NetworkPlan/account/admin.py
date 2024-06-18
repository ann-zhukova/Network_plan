from django.contrib import admin
from .models import CustomUser, Product, Stage, Project, Task, UserDoTask, Resource, TaskUseResource
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm


# Register your models here.

# from .models import Post
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', ]


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Product)
admin.site.register(Stage)
admin.site.register(UserDoTask)
admin.site.register(Resource)
admin.site.register(TaskUseResource)
