from django.db import models
from django.contrib.auth.models import AbstractUser # 继承django原有的用户属性字段


class User(AbstractUser):
    mobile = models.CharField(max_length=15, null=True, blank=True, verbose_name="手机号")
    avatar = models.ImageField(upload_to="avatar", null=True, blank=True, verbose_name="用户头像")

    class Meta:
        db_table = "user"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
