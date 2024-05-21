from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

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
    cover_image = models.ImageField(upload_to='videogame_covers/', blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

class Order(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    videogame_id = models.ForeignKey(VideoGame, on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    videogame = models.ForeignKey('VideoGame', on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField()