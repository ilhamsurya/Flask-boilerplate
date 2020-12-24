
from flask import Flask

app = Flask(__name__)

application = app = Flask(__name__, instance_relative_config="../instance")
app.config.from_pyfile("config.py")
