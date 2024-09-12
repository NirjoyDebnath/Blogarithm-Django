from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Story
from .serializers import CreateStorySerializer, StorySerializer, UpdateStorySerializer
from .permissions import IsAuthenticatedOrReadOnly, IsSameUserOrReadOnly


# Create your views here.

class CreateStory(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request):
        story = request.data
        user = request.user
        serializer = CreateStorySerializer(data={'author_id': user.id, 'author_username': user.username, 'title': story['title'], 'description': story['description'], "image": story.get('image', None)})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        all_stories = Story.objects.all()
        serializer = StorySerializer(all_stories, many=True)
        serialized_data = serializer.data
        return Response(serialized_data , status=status.HTTP_200_OK)

class StoryUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSameUserOrReadOnly]
    serializer_class = UpdateStorySerializer
    queryset = Story.objects.all()
