#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class Config():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    FILES_DIR = os.path.join(BASE_DIR, 'files')
    UPLOAD_DIR = os.path.join(FILES_DIR, 'uploads')
    DOWNLOAD_DIR = os.path.join(FILES_DIR, 'downloads')
    LOG_DIR = os.path.join(BASE_DIR, 'logs')


class Dev(Config):
    DEBUG = True
    DATABASE = {
        'host': 'localhost',
        'port': 3306,
        'user': 'docker',
        'passwd': 'docker',
        'db': 'todo'
    }
    # Flask-Sqlalchemy 配置
    SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{passwd}@{host}:{port}/{db}'.format(
        **DATABASE)
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
