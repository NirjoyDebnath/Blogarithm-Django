# Generated by Django 5.1.1 on 2024-09-09 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0011_alter_users_password_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password_modified_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 10, 0, 7, 51, 668937)),
        ),
    ]
