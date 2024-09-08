from django.db import models
import uuid
from users.models import User
import datetime

# Create your models here.

class Auth(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=25)
    password_modified_at = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = 'auth'
        constraints = [
            models.UniqueConstraint(fields=['username'], name='unique_auth_username'),
        ]

    def __str__(self):
        return self.username

