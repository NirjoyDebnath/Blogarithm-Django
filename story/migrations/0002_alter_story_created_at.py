# Generated by Django 5.1.1 on 2024-09-09 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 17, 55, 38, 267460)),
        ),
    ]
