# Generated by Django 5.1.1 on 2024-09-08 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_alter_user_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 0, 25, 14, 333278)),
        ),
    ]
