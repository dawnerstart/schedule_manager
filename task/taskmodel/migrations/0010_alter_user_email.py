# Generated by Django 3.2 on 2021-05-17 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmodel', '0009_auto_20210517_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
