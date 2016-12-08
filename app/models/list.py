#!/usr/bin/env python
# -*- coding: utf-8 -*-
from extension import db

class Todo(db.Model):
    __tablename__ = 'todo_list'
    id=db.Column(db.Integer,primary_key=True,unique=True,index=True)
    name=db.Column(db.String(256),nullable=False)
    desc=db.Column(db.String(1024),nullable=False)
    status=db.Column(db.SmallInteger(),nullable=False,default=0)
    create_time=db.Column(db.DateTime(),nullable=False)
    modify_time=db.Column(db.DateTime(),nullable=True)