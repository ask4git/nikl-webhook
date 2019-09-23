
# -*- coding: utf-8 -*-

# 입력데이터가 json이 아닐때
# key error

import traceback
import logging
from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
