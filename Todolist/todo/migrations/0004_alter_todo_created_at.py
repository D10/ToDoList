# Generated by Django 3.2.3 on 2021-05-18 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
    ]