from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    def handle(self, *args, **options):
        senior = Group(name='Senior')
        middle = Group(name='Middle')
        junior = Group(name='Junior')
        senior.save()
        middle.save()
        junior.save()
