from backend.database.conn import connect
from flask import request
import sqlite3

# Endpoint for seeing all mahasiswa
def seeMahasiswa():
    conn = connect()
    c = conn.cursor(dictionary=True)

    try:
        qty = request.args.get('qty')
        c.execute("SELECT * FROM mahasiswa LIMIT %s", (qty,))

    except:
        c.execute("SELECT * FROM mahasiswa")
    
    result = c.fetchall()
    if result is not None:
        for single in result:
            single['password'] = None

        result = result
    
    else:
        result = []

    conn.close()

    return { "msg": "Query successful",  "data": result }

# Endpoint for seeing one student
def seeMahasiswa(id):
    conn = connect()
    c = conn.cursor(dictionary=True)

    c.execute("SELECT * FROM mahasiswa WHERE id = %s", (id,))
    result = c.fetchone()
    conn.close()

    if result is not None:
        result['password'] = None
        return { "msg": "Query successful",  "data": result }
    
    else:
        return { "msg": "Not found" }
