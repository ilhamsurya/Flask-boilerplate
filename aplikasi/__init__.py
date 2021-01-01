# External imports
from flask import Flask, render_template, request
import os

# Flask app init
application = app = Flask(__name__, instance_relative_config="../instance")

# file import
from aplikasi.backend.api import *
from aplikasi.frontend import *

# config import
app.config.from_pyfile("config.py")

# Registering backend routes
app.register_blueprint(auth_api)
app.register_blueprint(mahasiswa_api, url_prefix="/api/mahasiswa")

# Registering frontend routes
app.register_blueprint(landing)
app.register_blueprint(mahasiswa)
# Registering api routes


# error pages
