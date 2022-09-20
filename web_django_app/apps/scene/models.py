from django.db import models


class Scene(models.Model):
    """ 场景模型 """
    name = models.CharField(max_length=100, verbose_name="场景名称")
    engname = models.CharField(max_length=100, verbose_name="场景英文简称")
    img_url = models.ImageField(upload_to="scene", null=True, blank=True, max_length=255, verbose_name="场景图片")
    intro = models.TextField(verbose_name="场景介绍")

    class Meta:
        db_table = "scene"
        verbose_name = "地点场景"
        verbose_name_plural = verbose_name