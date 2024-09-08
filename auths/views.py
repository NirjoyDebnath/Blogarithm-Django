from datetime import datetime

from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AuthandUserSerializer


# Create your views here.
@api_view(['POST'])
def sign_up(request):
    # user_id = request.data['user_id']
    # username = request.data['username']
    # password = request.data['password']
    # password_modified_at = datetime.now()
    serializer = AuthandUserSerializer(data = request.data)
    # return Response(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(request.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)