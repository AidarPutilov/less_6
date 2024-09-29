from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(email="admin@sky.pro")
        user.set_password("123qwe")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        user = User.objects.create(email="user1@sky.pro")
        user.set_password("123qwe")
        user.is_active = True
        user.save()
        user = User.objects.create(email="user2@sky.pro")
        user.set_password("123qwe")
        user.is_active = True
        user.save()
