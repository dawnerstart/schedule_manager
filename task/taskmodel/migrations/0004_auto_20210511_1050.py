# Generated by Django 3.2 on 2021-05-11 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmodel', '0003_auto_20210511_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='userid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='userid',
            field=models.IntegerField(),
        ),
    ]
