
# -*- coding: utf-8 -*-

from app import app
from flask import jsonify, request


@app.route('/', methods=['GET', 'POST'])
def index():
    return "hello!"

@app.route('/data')
def data():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)
