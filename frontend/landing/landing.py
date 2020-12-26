from flask import Blueprint, redirect, url_for, render_template, flash, Response
from backend.database.conn import connect
from datetime import datetime

landing = Blueprint('landing', __name__,
                    static_folder='static', template_folder='templates')


@landing.route("/")
def home():
    title = 'Sistem Kompetensi Mahasiswa'
    return render_template("/landing/index.html", title=title)


@landing.route("/login")
def login():
    title = 'Sistem Kompetensi Mahasiswa - Login'
    return render_template("/auth/login.html", title=title)


@landing.route("/register")
def register():
    title = 'Sistem Kompetensi Mahasiswa - Register'
    return render_template("/auth/register.html", title=title)


@landing.route("/forgot")
def forgot():
    title = 'Sistem Kompetensi Mahasiswa - Forgot Password'
    return render_template("/auth/forgot.html", title=title)
