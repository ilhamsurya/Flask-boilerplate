from flask import (
    Blueprint,
    Response,
    request,
    session,
    render_template,
    url_for,
    redirect,
)
from aplikasi.backend.query import seeOneMahasiswa
from aplikasi.backend.helper.decorator import login_required

mahasiswa = Blueprint("mahasiswa", __name__, template_folder="templates")


@mahasiswa.route("/dashboard/<username>")
@login_required
def dashboard_siswa(username):
    if session.get("access"):
        return redirect("/login")

    title = "DASHBOARD MAHASISWA"
    data = seeOneMahasiswa(session["id"])
    return render_template(
        "mahasiswa/index.html", title=title, data=data["data"], uname=username
    )


@mahasiswa.route("/register/mahasiswa")
def register():
    title = "Sistem Kompetensi Mahasiswa - Register"
    return render_template("mahasiswa/register.html", title=title)
