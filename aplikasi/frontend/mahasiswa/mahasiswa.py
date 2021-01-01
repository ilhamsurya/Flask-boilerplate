from flask import Blueprint, Response, request, session, render_template, url_for
from aplikasi.backend.query import seeOneMahasiswa
from aplikasi.backend.helper.decorator import login_required

mahasiswa = Blueprint("mahasiswa", __name__, template_folder="templates")


@mahasiswa.route("/<username>")
@login_required
def dashboard_siswa(username):
    title = "SDKM - {username}"
    data = seeOneMahasiswa(session["id"])
    return render_template(
        "mahasiswa/index.html",
        title=title,
        data=data["data"],
        uname=username,
    )
