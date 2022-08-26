def jwt_response_payload_handler(token, user = None, request = None):
    """
    自定义 jwt认证成功 返回数据
    :param token    本次登陆成功后，返回的jwt
    :param user     本次登陆成功后，从数据库中查询到的用户模型信息
    :param request  本次客户端的请求对象（包含请求地址等等信息）
    """
    return {
        'token': token,
        'id': user.id,
        'username': user.username,
    }

from .models import User
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
class UsernameMobileAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = User.objects.filter( Q(username = username) | Q(mobile = username) ).first()
        if user and user.check_password(password) and user.is_authenticated:
            return user
        else:
            return None