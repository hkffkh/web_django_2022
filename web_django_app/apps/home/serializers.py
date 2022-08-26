from rest_framework import serializers
from .models import Banner, Nav

class BannerModelSerializer(serializers.ModelSerializer):
    """轮播图的序列化器"""
    class Meta:
        model = Banner
        fields = ["image_url", "link"]

class NavModelSerializer(serializers.ModelSerializer):
    """导航菜单序列化器"""
    class Meta:
        model = Nav
        fields = ["title", "link", "is_site"]