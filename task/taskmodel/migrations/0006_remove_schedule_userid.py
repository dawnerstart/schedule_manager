# Generated by Django 3.2 on 2021-05-17 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmodel', '0005_schedule_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='userid',
        ),
    ]
