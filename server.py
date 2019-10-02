"""
server.py
"""
# -*- coding: utf-8 -*-

import logging
from app import app

HOST = '0.0.0.0'
PORT = 80

if __name__ == '__main__':
    try:
        app.run(host=HOST, port=PORT, debug=False)
    except Exception as e:
        logging.exception('error!')   # logging
