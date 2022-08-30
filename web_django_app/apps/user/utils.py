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
from django.contrib.auth.backends import ModelBackend
import re

def get_user_by_account(account):
    """
    根据账号获取user对象
    :param account: 账号，可以是用户名，也可以是手机号
    :return: User对象 或者 None
    """
    try:
        if re.match('^1[3-9]\d{9}$', account):
            # 帐号为手机号
            user = User.objects.get(mobile=account)
        else:
            # 帐号为用户名
            user = User.objects.get(username=account)
    except User.DoesNotExist:
        return None
    else:
        return user

class UsernameMobileAuthBackend(ModelBackend):
    """
    用户名或手机号认证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_account(username)
        if user is not None and user.check_password(password):
            return user
