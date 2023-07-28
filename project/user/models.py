import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from project.user.manager import UserManager


class User(AbstractUser):
    username = models.UUIDField(
        max_length=150,
        unique=True,
        error_messages={
            'unique': "A user with that username already exists.",
        },
        default=uuid.uuid4
    )
    email = models.EmailField(max_length=150, unique=True, error_messages={
        'unique': "A user with that email already exists.",
    },)
    name = models.CharField(max_length=150, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        if not self.name and self.is_active:
            split_email = self.email.split("@")[0]
            if len(split_email) <= 150:
                self.name = split_email.title()
        instance = super().save(*args, **kwargs)
        return instance
