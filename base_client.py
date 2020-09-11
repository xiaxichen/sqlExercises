import os
from configparser import ConfigParser

import pymysql
curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "config.ini")

config = ConfigParser()
config.read(cfgpath, encoding="utf-8")

mysqlOption = dict(config.items("MYSQL_SETTING"))

connect = pymysql.connect(host=mysqlOption.get("host_name"), port=int(mysqlOption.get("port")),
                          user=mysqlOption.get("user"), password=mysqlOption.get("password"),
                          db=mysqlOption.get("db_name"), charset=mysqlOption.get("charset"))