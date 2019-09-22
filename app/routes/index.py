
# -*- coding: utf-8 -*-

from app import app
from app import to_slack as ts
from flask import request, jsonify


@app.route('/', methods=['POST'])
def index():
    json_data = request.json
    ts.send_to_slack(json_data)
    return "대창구이 먹고싶다ㅎ"
