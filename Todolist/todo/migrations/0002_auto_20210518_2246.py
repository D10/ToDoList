# Generated by Django 3.2.3 on 2021-05-18 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='priority',
            options={'verbose_name': 'Приоритет', 'verbose_name_plural': 'Приоритеты'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.AddField(
            model_name='priority',
            name='color',
            field=models.CharField(default=1, max_length=20, verbose_name='Цвет'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='status',
            name='icon',
            field=models.CharField(default=43, max_length=50, verbose_name='Иконка'),
            preserve_default=False,
        ),
    ]
