# Generated by Django 5.1.1 on 2024-09-08 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_auth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 12, 59, 6, 263724)),
        ),
    ]
