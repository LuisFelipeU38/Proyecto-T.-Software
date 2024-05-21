# serializers.py
from rest_framework import serializers
from .models import VideoGame

class VideoGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGame
        fields = ['id', 'title', 'dev', 'category', 'stock', 'price', 'rating', 'cover_image']
