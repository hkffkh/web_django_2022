from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView

from .models import User
from .serializers import UserModelSerializer
from .utils import get_user_by_account
from rest_framework import status

class UserAPIView(CreateAPIView):
    """用户信息视图"""
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


"""
GET /user/mobile/<mobile>/
"""
class MobileAPIView(APIView):
    def get(self, request, mobile):
        ret = get_user_by_account(mobile)
        if ret is not None:
            return Response({"message":"该手机号已被注册！"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)