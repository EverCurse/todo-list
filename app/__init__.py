#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from jinja2.utils import import_string
from app.views.main import main
blueprints=[
   'app.views.main:main',None
]
def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    load_config(app)
    load_ext(app)
    #register_blueprints(app)
    return app


def load_config(app):
    app.config.from_object('config.Dev')


def load_ext(app):
    from app.views.apis import api
    from extension import db
    api.init_app(app)
    db.init_app(app)

def register_blueprints(app):
    for bp_info in blueprints:
        bp = import_string(bp_info[0])
        app.register_blueprint(bp,url_prefix=bp_info[1])