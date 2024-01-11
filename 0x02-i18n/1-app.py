#!/usr/bin/env python3
"""using the flask_babel"""
from flask_babel import Babel
import flask
app = flask.Flask(__name__)
babel = Babel().init_app(app)

class Config():
    LANGUAGES = ["en", "fr"]

app.run('0.0.0.0', 5000)
