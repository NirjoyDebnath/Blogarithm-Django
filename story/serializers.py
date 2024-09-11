from rest_framework import serializers
from .models import Story
from django.contrib.auth import authenticate

class CreateStorySerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=3, max_length=50)
    description = serializers.CharField(min_length=3, max_length=500)

    class Meta:
        model = Story
        fields = ['author_id', 'title', 'description', 'author_username']


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'author_id', 'title', 'description', 'author_username', 'created_at']

class UpdateStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['title', 'description']

