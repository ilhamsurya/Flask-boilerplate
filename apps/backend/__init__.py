from flask import Flask
from apps.backend.database.conn import connect
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return {
        'name': 'Welcome To FLASK'
    }


if __name__ == '__main__':
    app.run()
