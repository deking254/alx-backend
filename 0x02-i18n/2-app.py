#!/usr/bin/env python3
"""using the flask_babel"""
from flask_babel import Babel
from flask import Flask, request
app = Flask(__name__)
babel = Babel(app)


class Config():
    """the configuration class for the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

@babel.localeselector
@app.route('/')
def get_locale():
    """get the locale from request"""
    a = request.accept_languages
    t = a.best_match(app.config['LANGUAGES'])
    return 'The best fit locale is {}'.format(t)
