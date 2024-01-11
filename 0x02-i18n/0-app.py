#!/usr/bin/env python3
"""this is a module to create a simple flask app"""
from flask import Flask
import flask
import templates
app = Flask(__name__)
print(app)


@app.route('/')
def index():
    return flask.render_template("0-index.html")
app.run('0.0.0.0', '5000')
