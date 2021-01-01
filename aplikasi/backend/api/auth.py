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
        flash("You are now logged in", "success")
        return redirect(f"/{result['username']}")

    # Compare Passwords
    if sha256_crypt.verify(password, result["password"]):
        # Passed
        session["id"] = result["id"]
        session["token"] = makeToken(session["id"])
        session["username"] = username

        flash("You are now logged in", "success")
        return redirect(f"/{result['username']}")

    else:
        flash("You are now logged in", "success")
        return redirect(f"/{result['username']}")


# Endpoint for logging out
@auth_api.route("/logout")
def logout():
    session["token"] = None
    session.clear()
    return redirect("/")
