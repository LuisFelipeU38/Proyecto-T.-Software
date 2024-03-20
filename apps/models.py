from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username}"

class VideoGame(models.Model):
    title = models.CharField(max_length=255)
    dev = models.CharField(max_length=255)
    category = models.CharField(max_length=60)
    stock = models.IntegerField()
    price = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.title}"

class Order(models.Model):
    user_id = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    videogame_id = models.ForeignKey(VideoGame, on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)