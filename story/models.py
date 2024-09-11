from django.db import models
from customuser.models import Users
import uuid
import datetime

class Story(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author_username = models.CharField(max_length=25)
    created_at = models.DateTimeField(default=datetime.datetime.now())

    REQUIRED_FIELDS = ['title', 'description', 'author_username', 'author_id']

    def __str__(self):
        return str(self.author_id)