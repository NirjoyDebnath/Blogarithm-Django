# Generated by Django 5.1.1 on 2024-09-08 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0026_alter_auth_password_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='password_modified_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 0, 35, 24, 697563)),
        ),
    ]
