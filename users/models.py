from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    country = models.CharField(
        max_length=35,
        verbose_name="страна",
        blank=True,
        null=True,
        help_text="Введите страну",
    )
    phone = models.CharField(
        max_length=35,
        verbose_name='телефон',
        blank=True,
        null=True,
        help_text='Введите номер телефона'
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="аватар",
        blank=True,
        null=True,
        help_text="Загрузите свой аватар",
    )
    token = models.CharField(
        max_length=100,
        verbose_name='токен',
        blank=True,
        null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.email
