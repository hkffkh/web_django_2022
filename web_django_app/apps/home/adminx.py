import xadmin
from xadmin import views


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "xxx站点标题"  # 设置站点标题
    site_footer = "xxxx站点页脚"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)

# 轮播图
from .models import Banner


class BannerModelAdmin(object):
    list_display = ["title", "orders", "is_show", "scene"]
    list_filter = ["scene__id"]

xadmin.site.register(Banner, BannerModelAdmin)


# 导航菜单
from .models import Nav


class NavModelAdmin(object):
    list_display = ["title", "link", "is_show", "is_site", "position"]


xadmin.site.register(Nav, NavModelAdmin)

# 场景地点
from scene.models import Scene


class SceneModelAdmin(object):
    list_display = ["name", "engname", "img_url", "intro"]

xadmin.site.register(Scene, SceneModelAdmin)
