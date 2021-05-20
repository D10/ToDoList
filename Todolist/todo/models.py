from django.db import models
from datetime import datetime


class Priority(models.Model):
    name = models.CharField(max_length=150, verbose_name='Приоритет')
    color = models.CharField(max_length=20, verbose_name='Цвет')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Приоритет'
        verbose_name_plural = 'Приоритеты'


class Status(models.Model):
    name = models.CharField(max_length=150, verbose_name='Статус')
    icon = models.CharField(max_length=50, verbose_name='Иконка')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class ToDo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    will_end = models.DateTimeField(verbose_name='Дата выполнения')
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, verbose_name='Приоритет')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    name = models.CharField(max_length=250, verbose_name='Название задачи')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']
