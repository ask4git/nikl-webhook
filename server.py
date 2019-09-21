
# -*- coding: utf-8 -*-

from app import app

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8000, debug=True)

from flask import Flask
application = Flask(__name__)

@application.route("/")
def index():
    return "Hello JinHyuk!"


if __name__ == "__main__":
    application.run(host='0.0.0.0', port='8000')
