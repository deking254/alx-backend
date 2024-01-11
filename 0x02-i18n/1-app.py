#!/usr/bin/env python3
"""using the flask_babel"""
from flask_babel import Babel
import flask
babel = Babel()


class Config():
    LANGUAGES = ["en", "fr"]
app = flask.Flask(__name__)
app.run('0.0.0.0', 5000)
