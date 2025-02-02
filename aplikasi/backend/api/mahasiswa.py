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
from aplikasi.backend.query import seeMahasiswa, seeOneMahasiswa
from aplikasi.backend.helper.decorator import login_required


mahasiswa_api = Blueprint("mahasiswa_api", __name__)

# Endpoint Buat Mahasiswa


# Liat semua Mahasiswa
@mahasiswa_api.route("/", methods=["GET"])
def AllMahasiswa():
    response = seeMahasiswa()
    data = response.get("data", None)

    if data is None:
        return Response(
            response='{"msg": "user not found"}',
            status=400,
            content_type="application/json",
        )
    else:
        return {"msg": "Query Successful", "data": data}


# Liat Profil Mahasiswa
@mahasiswa_api.route("/<int:id>", methods=["GET"])
def ProfilMahasiswa(id):
    response = seeOneMahasiswa(id)
    data = response.get("data", None)

    if data is None:
        return Response(
            response='{"msg": "user not found"}',
            status=400,
            content_type="application/json",
        )
    else:
        return {"msg": "Query Successful", "data": data}


# Tambah Mahasiswa
@mahasiswa_api.route("/new", methods=["POST"])
def createMahasiswa():

    try:
        conn = connect()
        c = conn.cursor(dictionary=True)

        username = request.form["username"]
        password = sha256_crypt.encrypt(request.form["password"])
        name = request.form["name"]
        nim = request.form["nim"]
        email = request.form["email"]
        phone = request.form["phone"]
        jurusan_id = request.form["jurusan_id"]
        prodi_id = request.form["prodi_id"]

        c.execute(
            "SELECT * FROM mahasiswa WHERE username = %s or email = %s or phone = %s",
            (username, email, phone),
        )

        if c.fetchone() is not None:
            flash(
                "Data sudah digunakan, masukkan username, email, atau nomor HP yang berbeda"
            )
            return redirect(request.referrer)

        c.execute(
            """
        INSERT INTO mahasiswa ( 
            username, password, name, nim, email, phone, jurusan_id, prodi_id, createdAt, updatedAt 
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """,
            (
                username,
                password,
                name,
                nim,
                email,
                phone,
                jurusan_id,
                prodi_id,
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


# Endpoint for updating a student
@mahasiswa_api.route("/<int:id>", methods=["POST"])
@login_required
def updateMahasiswa(id):
    conn = connect()
    c = conn.cursor(dictionary=True)

    if request.form["password"] != "":
        new_password = sha256_crypt.encrypt(request.form["password"])
        email = request.form["email"]
        phone = request.form["phone"]
        name = request.form["name"]
        nim = request.form["nim"]
        jurusan_id = request.form["jurusan_id"]
        prodi_id = request.form["prodi_id"]

        c.execute(
            """
        UPDATE mahasiswa SET 
        email = %s, 
        password = %s, 
        phone = %s, 
        name = %s,  
        nim = %s,
        jurusan_id = %s,
        prodi_id = %s,
        updatedAt = %s
        WHERE id = %s
        """,
            (
                email,
                new_password,
                phone,
                name,
                nim,
                jurusan_id,
                prodi_id,
                datetime.now(),
                id,
            ),
        )
    else:
        email = request.form["email"]
        phone = request.form["phone"]
        name = request.form["name"]
        nim = request.form["nim"]
        jurusan_id = request.form["jurusan_id"]
        prodi_id = request.form["prodi_id"]

        c.execute(
            """
        UPDATE mahasiswa SET 
        email = %s, 
        phone = %s, 
        name = %s,  
        nim = %s,
        jurusan_id = %s,
        prodi_id = %s,
        updatedAt = %s
        WHERE id = %s
        """,
            (
                email,
                phone,
                name,
                nim,
                jurusan_id,
                prodi_id,
                datetime.now(),
                id,
            ),
        )
    conn.commit()
    conn.close()

    return redirect(request.referrer)


# Endpoint for updating a student
@mahasiswa_api.route("/<int:id>", methods=["DELETE"])
@login_required
def deleteMahasiswa(id):
    conn = connect()
    c = conn.cursor(dictionary=True)

    c.execute("SELECT * FROM mahasiswa WHERE id = %s", (id,))
    result = c.fetchone()
    result["password"] = None

    c.execute("DELETE FROM mahasiswa WHERE id = %s", (id,))
    conn.commit()
    c.close()

    return {"msg": "Mahasiswa berhasil dihapus", "data": result}
