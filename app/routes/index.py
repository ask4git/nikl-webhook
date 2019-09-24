"""
index.py
"""
# -*- coding: utf-8 -*-

from app import app
from app import to_slack as ts
from app import to_gsheet as tg
from flask import request, jsonify


@app.route('/', methods=['POST'])
def index():
    json_data = request.json
    ts.send_to_slack(json_data)
    tg.send_to_gsheet(json_data)
    return "success"
