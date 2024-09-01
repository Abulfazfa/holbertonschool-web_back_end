#!/usr/bin/env python3
"""
This module sets up a Flask application with Babel for internationalization.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Config class to set available languages, default locale, and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Accept-Language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    The index route that returns the rendered index.html template.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()