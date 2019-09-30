"""
server.py
"""
# -*- coding: utf-8 -*-

import logging
from app import app

HOST = '127.0.0.1'
PORT = 8000

if __name__ == '__main__':
    try:
        app.run(host=HOST, port=PORT, debug=False)
    except Exception as e:
        logging.exception('error!')   # logging
