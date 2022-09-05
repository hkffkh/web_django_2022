from django.db.models import Q
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import obtain_jwt_token
from .utils import get_user_by_account


class UserModelSerializer(serializers.ModelSerializer):
    """用户注册信息序列化器"""
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['token', 'id', 'username', 'password']
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def validate(self, attrs):
        username = attrs.get("username")
        # 验证用户名是否被注册
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user is not None:
            raise serializers.ValidationError("该用户名已被注册！")

        return attrs

    def create(self, validated_data):
        """用户信息，创建用户"""
        # validated_data.pop("sms_code")  # 去除验证码，其余内容保留，需要存至数据库
        # 对密码hash加密
        raw_password = validated_data.get("password")
        hash_password = make_password(raw_password)
        username = validated_data.get("username")
        user = User.objects.create(
            username=username,
            password=hash_password,
        )

        # 使用restframework_jwt模块提供的手动生成token的方法生成登陆状态
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        user.token = jwt_encode_handler(payload)
        # 调用序列化器提供的create方法

        return user

    def get_token(self, user):
        return user.token
