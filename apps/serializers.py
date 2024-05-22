from rest_framework import serializers
from .models import VideoGame

class VideoGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VideoGame
        fields = ['id', 'title', 'dev', 'category', 'stock', 'price', 'rating', 'cover_image', 'url']
        extra_kwargs = {
            'url': {'view_name': 'videogame-detail', 'lookup_field': 'pk'}
        }

