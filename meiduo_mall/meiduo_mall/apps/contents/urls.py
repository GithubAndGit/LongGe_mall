from django.urls import re_path
from . import views

urlpatterns = [
    # 首页广告: reverse(contents:index) == '/'
    re_path(r'^$', views.IndexView.as_view(), name='index'),
]
