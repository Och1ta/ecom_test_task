# Generated by Django 5.0.4 on 2024-04-22 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название склада')),
                ('location', models.CharField(max_length=100, verbose_name='Местоположение склада')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название оборудования')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество оборудования')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouses.category', verbose_name='Название категории')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouses.stock', verbose_name='Название склада')),
            ],
        ),
    ]
