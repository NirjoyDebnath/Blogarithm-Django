from datetime import datetime

from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


# Create your views here.
@api_view(['POST'])
def sign_up(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)