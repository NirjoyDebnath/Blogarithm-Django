from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
import datetime
import uuid


class UsersManager(BaseUserManager):

    def create_user(self, email, name, username, password=None):
        if email is None:
            raise TypeError('Users should have a Email')

        # user = self.model(email=self.normalize_email(email))
        user = self.model(email = email, name=name, username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, username, password=None):
        if email is None:
            raise TypeError('Users should have a Email')
        if password is None:
            raise TypeError('Password should not be none')

        user = self.model(email = email, name=name, username=username)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class Users(AbstractUser, PermissionsMixin):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    password_modified_at = models.DateTimeField(default=datetime.datetime.now())

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username']

    objects = UsersManager()

    def __str__(self):
        return str(self.id)