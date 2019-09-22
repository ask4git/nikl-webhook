
# -*- coding: utf-8 -*-

from app import app
from flask import jsonify, request


@app.route('/', methods=['GET', 'POST'])
def index():
    return "대창구이 존맛!"
