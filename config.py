DEBUG = True
#MySQL Database
HOST = '192.168.141.10'
PORT = '3306'
USERNAME = 'root'
PASSWORD = '121468wang'
DATABASE = 'flask_cmdb'

DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset-utf8'.format(username=USERNAME,
                                                                                        password=PASSWORD,
                                                                                        host=HOST,
                                                                                        port=PORT,
                                                                                        db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
#配置一个key为session加密用
import os
from datetime  import  timedelta
#session
SECRET_KEY = os.urandom(24)
#设置session有效期为2天，若开启了session.permanent后不设置该参数，则默认为31天
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
#配置统一的user_id,所有用到user_id的地方都要import config
CMDB_USER_ID = 'HEBOANHEHE'