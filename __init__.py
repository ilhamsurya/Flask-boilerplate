# External imports
from backend.api import *
from frontend import *
from flask import Flask, render_template, request
import os

# Flask app init
application = app = Flask(
    __name__, instance_relative_config="backend/instance")

# Registering backend routes
app.register_blueprint(student_routes)

# Registering frontend routes


# error pages
