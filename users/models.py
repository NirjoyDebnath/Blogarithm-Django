import datetime
from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    join_date = models.DateTimeField(default=datetime.datetime.now())
    role = models.IntegerField(default=0)

    class Meta:
        db_table = 'users'
        constraints = [
            models.UniqueConstraint(fields=['username'], name='unique_username'),
            models.UniqueConstraint(fields=['email'], name='unique_email'),
        ]

    def __str__(self):
        return str(self.id)

