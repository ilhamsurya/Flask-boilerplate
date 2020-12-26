import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

class config(object):
    

if os.environ.get('env', None) == "PRODUCTION":
    SECRET_KEY= os.enviro.get('SECRET_KEY')
    MYSQL_ROOT_USER = os.environ['MYSQL_ROOT_USER']
    MYSQL_ROOT_PASSWORD = os.environ['MYSQL_ROOT_PASSWORD']
    MYSQL_HOST = 'db'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(hours=8)
    DEBUG = True

else:
    MYSQL_ROOT_USER = 'root'
    MYSQL_ROOT_PASSWORD = ''
    MYSQL_HOST = 'localhost'
    MYSQL_DATABASE = 'aplikasita'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(hours=8)
    DEBUG = True
