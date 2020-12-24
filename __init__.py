from flask import Flask
from apps import app as application

app = flask.Flask("__main__")


@app.route('/api', methods=['GET'])
def index():
    return {
        'name': 'Welcome To FLASK'
    }


if __name__ == '__main__':
    app.run()
