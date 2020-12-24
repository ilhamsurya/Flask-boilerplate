import mysql.connector
from instance.config import MYSQL_ROOT_PASSWORD, MYSQL_ROOT_USER, MYSQL_HOST, MYSQL_DATABASE

config = {
    "user": MYSQL_ROOT_USER,
    "password": MYSQL_ROOT_PASSWORD,
    "database": MYSQL_DATABASE,
    "host": MYSQL_HOST
}

def connect(config=config):
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
    except:
        conn = None

    return conn
