"""
server.py
"""
# -*- coding: utf-8 -*-

import logging
from app import app


if __name__ == '__main__':
    try:
        app.run(host='127.0.0.1', port=8000, debug=False)
    except Exception as e:
        logging.exception('error!')   # logging
