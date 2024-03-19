from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_normal_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.is_normal_user:
                self.is_staff = False
                self.is_superuser = False
            elif self.is_admin:
                self.is_staff = True
                self.is_superuser = False
        super().save(*args, **kwargs)

