from django.db import models
from customuser.models import Users
import uuid
import datetime
import os

def generate_unique_filename(instance, filename):
    ext = os.path.splitext(filename)[1]
    unique_filename = f"{uuid.uuid4()}{ext}"
    return os.path.join('images/stories/', unique_filename)

class Story(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author_username = models.CharField(max_length=25)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    image = models.ImageField(upload_to=generate_unique_filename, blank=True, null=True)

    REQUIRED_FIELDS = ['title', 'description', 'author_username', 'author_id']

    def __str__(self):
        return str(self.author_id)