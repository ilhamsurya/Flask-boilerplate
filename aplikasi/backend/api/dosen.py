from flask import (
    Blueprint,
    redirect,
    url_for,
    render_template,
    flash,
    Response,
    request,
)
from passlib.hash import sha256_crypt
from datetime import datetime
from aplikasi.backend.database.conn import connect
from aplikasi.backend.query import seeDosen, seeOneDosen
from aplikasi.backend.helper.decorator import login_required

dosen_api = Blueprint("dosen_api", __name__)

# Liat semua Dosen
@dosen_api.route("/", methods=["GET"])
def AllDosen():
    response = seeDosen()
    data = response.get("data", None)

    if data is None:
        return Response(
            response='{"msg": "user not found"}',
            status=400,
            content_type="application/json",
        )
    else:
        return {"msg": "Query Successful", "data": data}


# Liat Profil Dosen
@dosen_api.route("/<int:id>", methods=["GET"])
def ProfilDosen(id):
    response = seeOneDosen(id)
    data = response.get("data", None)

    if data is None:
        return Response(
            response='{"msg": "user not found"}',
            status=400,
            content_type="application/json",
        )
    else:
        return {"msg": "Query Successful", "data": data}


# Tambah Dosen
@dosen_api.route("/new", methods=["POST"])
def createDosen():

    try:
        conn = connect()
        c = conn.cursor(dictionary=True)

        username = request.form["username"]
        password = sha256_crypt.encrypt(request.form["password"])
        name = request.form["name"]
        nip = request.form["nip"]
        email = request.form["email"]
        phone = request.form["phone"]
        access = "dosen"

        c.execute(
            "SELECT * FROM dosen WHERE username = %s or email = %s or phone = %s",
            (username, email, phone),
        )

        if c.fetchone() is not None:
            flash(
                "Data sudah digunakan, masukkan username, email, atau nomor HP yang berbeda"
            )
            return redirect(request.referrer)

        c.execute(
            """
        INSERT INTO dosen ( 
            username, password, name, nip, email, phone, access, createdAt, updatedAt
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """,
            (
                username,
                password,
                name,
                nip,
                email,
                phone,
                access,
                datetime.now(),
                datetime.now(),
            ),
        )

        conn.commit()
        conn.close()
        return redirect("/login")

    except:
        flash(
            "Data sudah digunakan, masukkan username, email, atau nomor HP yang berbeda"
        )
        return redirect(request.referrer)


# Endpoint for updating a Dosen
@dosen_api.route("/<int:id>", methods=["POST"])
@login_required
def updateDosen(id):
    conn = connect()
    c = conn.cursor(dictionary=True)

    if request.form["password"] != "":
        new_password = sha256_crypt.encrypt(request.form["password"])
        email = request.form["email"]
        phone = request.form["phone"]
        name = request.form["name"]
        nip = request.form["nip"]

        c.execute(
            """
        UPDATE dosen SET 
        email = %s, 
        password = %s, 
        phone = %s, 
        name = %s,  
        nip = %s,
        updatedAt = %s
        WHERE id = %s
        """,
            (
                email,
                new_password,
                phone,
                name,
                nip,
                datetime.now(),
                id,
            ),
        )
    else:
        email = request.form["email"]
        phone = request.form["phone"]
        name = request.form["name"]
        nip = request.form["nip"]

        c.execute(
            """
        UPDATE dosen SET 
        email = %s, 
        phone = %s, 
        name = %s,  
        nip = %s,
        updatedAt = %s
        WHERE id = %s
        """,
            (
                email,
                phone,
                name,
                nip,
                datetime.now(),
                id,
            ),
        )
    conn.commit()
    conn.close()

    return redirect(request.referrer)


# Endpoint for deleting a dosen
@dosen_api.route("/<int:id>", methods=["DELETE"])
@login_required
def deleteDosen(id):
    conn = connect()
    c = conn.cursor(dictionary=True)

    c.execute("SELECT * FROM dosen WHERE id = %s", (id,))
    result = c.fetchone()
    result["password"] = None

    c.execute("DELETE FROM dosen WHERE id = %s", (id,))
    conn.commit()
    c.close()

    return {"msg": "dosen berhasil dihapus", "data": result}
