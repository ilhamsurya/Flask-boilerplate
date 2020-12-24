from flask import Flask
from apps import app as application

if __name__ == '__main__':
    application.run(debug=True)
