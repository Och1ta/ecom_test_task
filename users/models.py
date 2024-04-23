from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models


class User(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username', 'password',
    )

    email = models.EmailField(
        'Электронная почта',
        max_length=150,
        unique=True,
        validators=[EmailValidator],
    )
    username = models.CharField(
        'Имя пользователя',
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return '{} {}'.format(self.username, self.email)
