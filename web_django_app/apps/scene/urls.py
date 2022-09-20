from django.urls import path, re_path
from . import views

urlpatterns = [
    # path(r"register/", views.UserAPIView.as_view()),
    # re_path(r"parameter/(?P<scenename>)/", views.MobileAPIView.as_view()),
    path(r"para/ZJUTcricket/", views.ZJUTcricketAPIView.as_view()),
]