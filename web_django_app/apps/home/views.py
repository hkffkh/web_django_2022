from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .models import Banner, Nav
from .serializers import BannerModelSerializer, NavModelSerializer
class BannerListAPIView(ListAPIView):   # 自动导包
    """轮播视图"""
    queryset = Banner.objects.filter(is_show=True, is_deleted=False).order_by("-orders","-id")[:7] # order_by排序，负号：倒序排序
    serializer_class = BannerModelSerializer    # 序列化器


class HeaderNavListAPIView(ListAPIView):
    """顶部导航菜单视图"""
    queryset = Nav.objects.filter(is_show=True, is_deleted=False, position=1).order_by("orders","-id")[:5] # order_by排序，负号：倒序
    serializer_class = NavModelSerializer    # 序列化器


class FooterNavListAPIView(ListAPIView):
    """底部导航菜单视图"""
    queryset = Nav.objects.filter(is_show=True, is_deleted=False, position=2).order_by("orders","-id")[:5] # order_by排序，负号：倒序
    serializer_class = NavModelSerializer    # 序列化器