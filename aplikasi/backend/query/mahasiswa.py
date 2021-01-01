from aplikasi.backend.database.conn import connect
from flask import request
import sqlite3

# Endpoint for seeing all mahasiswa
def seeMahasiswa():
    conn = connect()
    c = conn.cursor(dictionary=True)
    try:
        qty = request.args.get("qty")
        c.execute(
            "SELECT name,email,phone,jurusan_id,prodi_id FROM mahasiswa LIMIT %s",
            (qty,),
        )

    except:
        c.execute("SELECT * FROM mahasiswa")

    result = c.fetchall()
    conn.close()

    return {"msg": "Query successful", "data": result}


# Endpoint for seeing all mahasiswa
def seeOneMahasiswa(id):
    conn = connect()
    c = conn.cursor(dictionary=True)
    c.execute(
        "SELECT name,email,phone,jurusan_id,prodi_id FROM mahasiswa WHERE nim = %s",
        (id,),
    )
    result = c.fetchone()
    conn.close()

    return {"msg": "Query successful", "data": result}

