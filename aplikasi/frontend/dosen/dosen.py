from flask import Blueprint, Response, request, session, render_template, url_for
from aplikasi.backend.query import seeOneDosen
from aplikasi.backend.helper.decorator import login_required, dosen_only

dosen = Blueprint("dosen", __name__, template_folder="templates")


@dosen.route("/dashboard")
@login_required
@dosen_only
def dashboard_dosen():
    if not session.get("access"):
        return redirect(url_for("login"))

    title = "Sistem Kompetensi - Dosen"
    data = seeOneDosen(session["id"])
    return render_template(
        "dosen/index.html",
        title=title,
        data=data["data"],
    )


@dosen.route("/register/dosen")
def register():
    title = "Sistem Kompetensi Mahasiswa - Register Dosen"
    return render_template("dosen/register.html", title=title)
