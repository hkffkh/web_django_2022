"""
Django settings for web_django_app project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 新增一个系统导包路径
# 把apps目录下的所有子应用设置为可以直接导包，那就需要把apps设置为默认导包路径
sys.path.insert(0, os.path.join(BASE_DIR,"web_django_app/apps"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&24^v^+tioth0(9aj5ga@9lb5#x!)!3!kda3yqc33xhtm3l9_0'

# SECURITY WARNING: don't run with debug turned on in production!
# （部署false，调试true）
# DEBUG = True
DEBUG = False

# （部署，调试模）
# ALLOWED_HOSTS = ['127.0.0.1']
# 修改项。允许所有的IP访问网络服务
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 跨域
    'corsheaders',

    # drf框架（实现API接口）：
    # 将请求的数据（如JSON格式）转换为模型类对象
    # 操作数据库
    # 将模型类对象转换为响应的数据（如JSON格式）
    'rest_framework',

    # xadmin相关
    'xadmin',
    'crispy_forms',
    'reversion',

    # 子应用
    "home",
    "user",
    "scene",
]

# CORS组的配置信息
CORS_ORIGIN_WHITELIST= (
    # 部分版本需要协议，"http://127.0.0.1:8080"
	'http://127.0.0.1:8080',
)
# 是否允许ajax跨域请求时携带cookie
CORS_ALLOW_CREDENTIALS = False


MIDDLEWARE = [
    # 跨域，中间件，必须放在第一行
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'web_django_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'web_django_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "USER": "only_web",
        "PASSWORD": "web2022",
        "NAME": "web2022"  # 数据库名
    }
}


# # 设置redis缓存
# CACHES = {
#     # 默认缓存
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         # 项目上线时,需要调整这里的路径
#         "LOCATION": "redis://127.0.0.1:6379/0", # 0号库
#
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     },
#     # 提供给xadmin或者admin的session存储
#     "session": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1", # 1号库
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     },
#     # 提供存储短信验证码
#     "sms_code":{
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/2",  # 2号库
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
#
# # 设置xadmin用户登录时,登录信息session保存到redis
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "session"


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

# 修改使用中文界面
LANGUAGE_CODE = 'zh-Hans'

# 修改时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# 访问静态文件的url地址前缀
STATIC_URL = '/static/'

# （调试模式） 设置django的静态文件目录
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR,"static")
# ]

# # （部署模式）修改项。指定需要收集的静态文件的位置
# # 即前端打包文件所在位置
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend/dist/"),
]
#
# # （部署模式）新增项。静态文件收集目录
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')


# 项目中存储上传文件的根目录[暂时配置]，注意，uploads目录需要手动创建否则上传文件时报错
MEDIA_ROOT=os.path.join(BASE_DIR,"web_django_app/uploads")
# 访问上传文件的url地址前缀
MEDIA_URL ="/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # 日志的格式
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    # 日志的过滤信息
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 日志的处理方式
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置，日志文件名，日志保存目录logs必须手动创建
            'filename': os.path.join(BASE_DIR, "logs/web.log"),
            # 日志文件的最大值，此处设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 日志文件的数量，设置最大日志数量为10
            'backupCount': 10,
            # 日志格式：详细格式
            'formatter': 'verbose'
        },
    },
    # 日志对象
    'loggers': {
        'django': {
            'handlers': ['console','file'],
            'propagate': True,
        },
    }
}


REST_FRAMEWORK = {
    # 异常处理
    'EXCEPTION_HANDLER': 'web_django_app.utils.exceptions.custom_exception_handler',

    # 登录认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

import datetime
JWT_AUTH = {
    # 设置jwt有效期
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    # 设置返回数据的格式
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'user.utils.jwt_response_payload_handler',
}

# # 实现多条件（用户名，手机号）登陆判断
# AUTHENTICATION_BACKENDS = [
#     'user.utils.UsernameMobileAuthBackend',
# ]

# 注册自定义用户模型 user\models.py 文件中ctrl+点击AbstractUser，进入auth\models.py, class User最后一行“AUTH_USER_MODEL”
AUTH_USER_MODEL = "user.User"   # “子应用名称.模型类名”