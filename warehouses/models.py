from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название категории'
    )

    def __str__(self):
        return self.name


class Stock(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название склада'
    )
    location = models.CharField(
        max_length=100,
        verbose_name='Местоположение склада'
    )

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название оборудования'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Название категории'
    )
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        verbose_name='Название склада'
    )
    quantity = models.IntegerField(
        default=0,
        verbose_name='Количество оборудования'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        verbose_name='Пользователь'
    )

    def __str__(self):
        return self.name
