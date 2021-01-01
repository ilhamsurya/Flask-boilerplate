import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))


if os.environ.get("env", None) == "PRODUCTION":
    SECRET_KEY = os.environ["SECRET_KEY"]
    MYSQL_ROOT_USER = os.environ["MYSQL_ROOT_USER"]
    MYSQL_ROOT_PASSWORD = os.environ["MYSQL_ROOT_PASSWORD"]
    MYSQL_HOST = "db"
    UPLOADED_PATH = os.path.join(basedir, "../aplikasi", "uploads", "photos")
    UPLOAD_FOLDER = os.path.join(basedir, "../aplikasi", "uploads", "profile")
    STATIC_FOLDER = os.path.join(basedir, "../aplikasi", "static")
    MAX_CONTENT_LENGTH = 1.5 * 1024 * 1024
    SESSION_COOKIE_NAME = "aplikasi-session"
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(hours=8)
    DEBUG = True

else:
    SECRET_KEY = "testingverysecretkeyauthorized"
    MYSQL_ROOT_USER = "root"
    MYSQL_ROOT_PASSWORD = "root"
    MYSQL_HOST = "localhost"
    UPLOADED_PATH = os.path.join(basedir, "../aplikasi", "uploads", "photos")
    UPLOAD_FOLDER = os.path.join(basedir, "../aplikasi", "uploads", "profile")
    STATIC_FOLDER = os.path.join(basedir, "../aplikasi", "static")
    MAX_CONTENT_LENGTH = 1.5 * 1024 * 1024
    SESSION_COOKIE_NAME = "studbud-session"
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(hours=8)
    DEBUG = True
