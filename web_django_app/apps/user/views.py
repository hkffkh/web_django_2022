from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import User
from .serializers import UserModelSerializer

class UserAPIView(CreateAPIView):
    """用户信息视图"""
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
