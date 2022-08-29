from django.db.models import Q
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework_jwt.settings import api_settings

class UserModelSerializer(serializers.ModelSerializer):
    """用户注册信息序列化器"""
    sms_code = serializers.CharField(label='手机验证码', required=True, allow_null=False, allow_blank=False, write_only=True)
    # password2 = serializers.CharField(label='确认密码', required=True, allow_null=False, allow_blank=False, write_only=True)
    class Meta:
        model = User
        fields = ['sms_code', 'mobile', 'password']
        extra_kwargs = {
            "password":{
                "write_only":True
            }
        }

    def validate(self, attrs):

        mobile = attrs.get("mobile")
        sms_code = attrs.get("sms_code")
        password = attrs.get("password")
        # 验证手机号是否被注册
        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            user = None
        if user is not None:
            raise serializers.ValidationError("该手机号已被注册！")

        # todo 验证短信验证码是否正确

        return attrs

    def create(self, validated_data):
        """用户信息，创建用户"""
        validated_data.pop("sms_code")  # 去除验证码，其余内容保留，需要存至数据库
        # 对密码hash加密
        raw_password = validated_data.get("password")
        hash_password = make_password(raw_password)
        mobile = validated_data.get("mobile")
        # 调用序列化器提供的create方法
        user = User.objects.create(
            mobile=mobile,
            username=mobile,   # 用户名初始默认（手机号）
            password=hash_password,
        )

        # 使用restframework_jwt模块提供的手动生成token的方法生成登陆状态
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        user.token = jwt_encode_handler(payload)

        return user
