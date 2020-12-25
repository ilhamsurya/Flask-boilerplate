import mysql.connector as mysql

def connect():
    try:
        conn = mysql.connect(
            user = "root",
            password = "",
            database = "",
            host = "localhost"
        )
        print(conn)
        
    except:
        conn = None

    return conn
