#!/usr/bin/env python3
"""this is a module to create a simple flask app"""
from flask import Flask
app = Flask(__name__)
a = app.route('/')
