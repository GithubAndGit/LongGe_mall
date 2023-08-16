import pymysql
# pymysql.version_info = (3, 3, 13, "final", 0)     # 根据mysqlclient模块的版本来的，如果版本是2.1.1就不用这行代码，如果是2.2.0就需要。
pymysql.install_as_MySQLdb()