from flask import Flask
from database.conn import connect

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def index():
    return {
        'name': ['Welcome To FLASK', 'Selamat Datang Di Flask']
    }


if __name__ == '__main__':
    app.run()
