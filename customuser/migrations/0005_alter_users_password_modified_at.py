# Generated by Django 5.1.1 on 2024-09-08 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0004_alter_users_password_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password_modified_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 0, 31, 28, 860103)),
        ),
    ]
