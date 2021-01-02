from flask import Blueprint, session, request, redirect, render_template, url_for, flash
from aplikasi.backend.database.conn import connect
from aplikasi.backend.helper.func import makeToken
from passlib.hash import sha256_crypt
from flask_wtf import FlaskForm


auth_api = Blueprint("auth_api", __name__)

# Endpoint for AUTH
@auth_api.route("/login", methods=["POST"])
def login_user():
    # Create cursor
    conn = connect()
    c = conn.cursor(dictionary=True)

    # Get Form Fields
    username = request.form["username"]
    password = request.form["password"]

    # Get user by username
    c.execute("SELECT * FROM mahasiswa WHERE username = %s", [username])
    result = c.fetchone()

    if result is None:
        c.execute("SELECT * FROM mahasiswa WHERE email = %s", [username])
        result = c.fetchone()

    if result is None:
        c.execute("SELECT * FROM dosen WHERE username = %s", [username])
        result = c.fetchone()

    if result is None:
        c.execute("SELECT * FROM dosen WHERE email = %s", [username])
        result = c.fetchone()

    if result is None:
        flash("failed logged in", "failed")
        return redirect("/login")

    # Compare Passwords
    if sha256_crypt.verify(password, result["password"]):
        session["id"] = result["id"]
        if result.get("access", None) is not None:
            session["token"] = makeToken(session["id"])
            session["access"] = result["access"]
            session["username"] = username

            if session["access"] == "dosen":
                session["token"] = makeToken(session["id"])
                return redirect(f"/dashboard")
        else:
            session["token"] = makeToken(session["id"])
            return redirect(f"/dashboard/{result['username']}")


# Endpoint for logging out
@auth_api.route("/logout")
def logout():
    session["token"] = None
    session.clear()
    return redirect("/")
