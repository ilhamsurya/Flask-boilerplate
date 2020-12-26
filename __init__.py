# External imports
from backend.api import *
from frontend import *
from flask import Flask, render_template, request
import os

# Flask app init
app = Flask(__name__)

# Registering backend routes
@app.route('/time')
def get_current_time():
    return {'time': time.time()}

# Registering frontend routes


# error pages
