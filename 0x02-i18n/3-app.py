#!/usr/bin/env python3
"""using the flask_babel"""
from flask_babel import Babel
import flask_babel
from flask import Flask, request, render_template
import jinja2
app = Flask(__name__)
babel = Babel(app)


class Config():
    """the configuration class for the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """this renders the index page"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """get the locale from request"""
    language = request.accept_languages
    best_match = language.best_match(app.config['LANGUAGES'])
    return best_match
