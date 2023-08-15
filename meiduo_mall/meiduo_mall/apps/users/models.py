from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """自定义用户模型类"""
    mobile = models.CharField(max_length=11, unique=True, verbose_name="手机号")

    class Meta:
        db_table = "tb_users"    # 自定义表名
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):    # 调试模型类是否正确,返回用户名,可写可不写
        return self.username
