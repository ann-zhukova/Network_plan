from django.contrib.auth.models import Group
from .models import Worker
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'username', 'email', 'position', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']