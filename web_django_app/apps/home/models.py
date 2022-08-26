from django.db import models


class BaseModel(models.Model):
    """公共模型"""
    is_show = models.BooleanField(default=False, verbose_name="是否显示")
    orders = models.IntegerField(default=1, verbose_name="排序")
    is_deleted = models.BooleanField(default=False, verbose_name="是否删除")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        # 设置当前模型为抽象模型，在数据迁移时数据库不会为其创建表
        abstract = True


class Banner(BaseModel, models.Model):
    """ 轮播图模型 """
    # 模型字段
    title = models.CharField(max_length=500, verbose_name="标题")
    link = models.CharField(max_length=500, verbose_name="链接")
    image_url = models.ImageField(upload_to="banner", null=True, blank=True, max_length=255, verbose_name="图片")
    remark = models.TextField(verbose_name="备注信息")


    # 表信息声明
    class Meta:
        db_table = "banner" # 数据库中创建时 表的名称
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    # 自定义方法[自定义字段或者自定义工具方法]
    def __str__(self):
        return self.title


class Nav(BaseModel, models.Model):
    """导航菜单模型"""
    POSITION_OPTION = (
        (1, "顶部导航"),
        (2, "底部导航"),
    )
    title = models.CharField(max_length=500, verbose_name="导航标题")
    link = models.CharField(max_length=500, verbose_name="导航链接")
    position = models.IntegerField(choices=POSITION_OPTION, default=1, verbose_name="导航位置")
    is_site = models.BooleanField(default=False, verbose_name="是否站外地址")

    class Meta:
        db_table = 'nav'
        verbose_name = '导航菜单'
        verbose_name_plural = verbose_name

    # 自定义方法[自定义字段或者自定义工具方法]
    def __str__(self):
        return self.title