# Generated by Django 5.1.1 on 2024-09-23 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, help_text='Введите страну', max_length=35, null=True, verbose_name='страна'),
        ),
    ]
