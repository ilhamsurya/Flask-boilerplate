from aplikasi.backend.database.conn import connect
from flask import request
import sqlite3

# Endpoint for seeing all mahasiswa
def seeDosen():
    conn = connect()
    c = conn.cursor(dictionary=True)
    try:
        qty = request.args.get("qty")
        c.execute(
            "SELECT name,email,phone,nip,access FROM dosen LIMIT %s",
            (qty,),
        )

    except:
        c.execute("SELECT * FROM dosen")

    result = c.fetchall()
    conn.close()

    return {"msg": "Query successful", "data": result}


# Endpoint for seeing all mahasiswa
def seeOneDosen(id):
    conn = connect()
    c = conn.cursor(dictionary=True)
    c.execute(
        "SELECT name,email,phone,nip,access FROM dosen WHERE id = %s",
        (id,),
    )
    result = c.fetchone()
    conn.close()

    return {"msg": "Query successful", "data": result}
