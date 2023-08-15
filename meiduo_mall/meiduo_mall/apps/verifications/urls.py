from django.urls import re_path
from . import views

urlpatterns = [
    # 图形验证码
    re_path('^image_codes/(?P<uuid>[\w-]+)/$', views.ImageCodeView.as_view())
]
