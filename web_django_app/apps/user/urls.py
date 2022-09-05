from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path(r"login/", obtain_jwt_token),
    path(r"register/", views.UserAPIView.as_view()),
    re_path(r"username/(?P<username>)/", views.MobileAPIView.as_view()),
]