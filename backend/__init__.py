# External imports
from backend.api import *
from frontend import *
from flask import Flask, render_template, request
import os

# Flask app init
app = Flask(__name__)

# Registering backend routes


@app.route('/')
def get_current_time():
    return {'time': 'Testing Flask'}

# Registering frontend routes


# error pages
