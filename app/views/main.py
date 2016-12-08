#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps
from flask import Blueprint,render_template,jsonify
from flask import request

main=Blueprint('main',__name__)

#api 鉴权装饰器，暂时没用
def check_auth(username,password):
    return username=='1' and password == '2'

def require_auth(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        auth=request.authorization
        if not auth:
            return jsonify({'status':'now allow'})
        elif not check_auth(auth.username,auth.password):
            return jsonify({'status': 'username or password not correct'})
        return f(*args,**kwargs)
    return decorated


@main.route('/')
def index():
    return render_template('index.html')