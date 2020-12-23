import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

# MYSQL_ROOT_USER: root
#       MYSQL_ROOT_PASSWORD: 9thT83srsS.r4/5KExOsP
#       XENDIT_KEY: xnd_production_j7ca5mHTMzJ5rFn3xNIVpcn9cWTVSzHwvsilWoa8zqZ7eIjqGOMR0bG29FQFY
#       CALLBACK_TOKEN: d916916038c07a017259a26015b32c515fd150b8277c09c0f750d9f5afa3031f
#       SECRET_KEY: b'\xf9\xf9\xc2{f\xfd\xb1\x13\xdbwre\x14\xbc\x92\xe3'

if os.environ.get('env', None) == "PRODUCTION":
    MYSQL_ROOT_USER = os.environ['MYSQL_ROOT_USER']
    MYSQL_ROOT_PASSWORD = os.environ['MYSQL_ROOT_PASSWORD']
    MYSQL_HOST = 'db'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(hours=8)
    DEBUG = True

else:
    MYSQL_ROOT_USER = 'root'
    MYSQL_ROOT_PASSWORD = ''
    MYSQL_HOST = 'localhost'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(hours=8)
    DEBUG = True
