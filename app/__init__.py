
# -*- coding: utf-8 -*-

from flask import Flask
import flask


app = Flask(__name__)

from app.routes import *
