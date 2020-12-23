from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return {
        'name': 'Welcome To FLASK'
    }


if __name__ == '__main__':
    app.run()
