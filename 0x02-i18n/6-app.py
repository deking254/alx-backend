#!/usr/bin/env python3
"""using the flask_babel"""
from flask_babel import Babel
import flask_babel
from flask import Flask, request, render_template
import jinja2
import flask
app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """the configuration class for the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """this renders the index page"""
    username = None
    if flask.g.get('user') is not None:
        username = flask.g.user.get('name')
    return render_template('6-index.html', username=username)


@babel.localeselector
def get_locale():
    """get the locale from request"""
    locale = None
    if request.args.get('locale') is not None:
        locale = request.args.get('locale')
    elif flask.g.get('user') is not None:
        locale = flask.g.get('user').get('locale')
    if locale is None:
        language = request.accept_languages
        best_match = language.best_match(app.config['LANGUAGES'])
        return best_match
    else:
        if locale in Config.LANGUAGES:
            return locale
        else:
            pass


@app.before_request
def before_request():
    """this function is the first to be called"""
    if request.args.get('login_as') is not None:
        user = get_user(int(request.args.get('login_as')))
        flask.g.user = user


def get_user(user_id: str):
    """returns a user if login_as parameter is used"""
    return users.get(user_id)
