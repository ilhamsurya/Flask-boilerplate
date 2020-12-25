from flask import Flask
from backend.database.conn import connect
app = Flask(__name__)

@app.route('/', methods=['GET'])
def api():
    return {
        'name': 'Welcome To FLASK'
    }


if __name__ == '__main__':
    app.run()
