from django.contrib import admin
from .models import CustomUser, VideoGame, Order
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(VideoGame)
admin.site.register(Order)