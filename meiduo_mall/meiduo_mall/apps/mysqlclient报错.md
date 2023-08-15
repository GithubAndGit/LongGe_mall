#### 报错
- django.core.exceptions.ImproperlyConfigured: mysqlclient 1.4.3 or newer is required; you have 1.0.2.

#### 解决方法
- 在应用层的__init__.py中加上这几行(如: D:\pycharm project\Django项目\meiduo_project\meiduo_mall\meiduo_mall\apps\users\__init__.py)
  - import pymysql

  - pymysql.install_as_MySQLdb()
> 如果还是不行加上
> pymysql.version_info = (3, 3, 13, "final", 0)
> 里面的前三个数字是版本信息，太低了就调高。