from configparser import ConfigParser

import pymysql

config = ConfigParser.ConfigParser()
config.read('config.ini')

mysql_list = config.options("MYSQL_SETTING")

connect = pymysql.connect(host=mysql_list.get("HOST_NAME"), port=mysql_list.get("HOST_NAME"),
                          user=mysql_list.get("USER"), password=mysql_list.get("PASSWORD"),
                          db=mysql_list.get("DB_NAME"), charset=mysql_list.get("CHARSET"))