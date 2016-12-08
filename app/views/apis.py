#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from extension import api, db
from flask import jsonify, request
from flask_restful import Resource
from app.models.list import Todo


class all_list(Resource):

    def get(self):
        lists = Todo.query.all()
        res = []
        for i in lists:
            if i.status == 0:
                status = u'新建'
            elif i.status == 1:
                status = u'进行中'
            elif i.status == 2:
                status = u'已完成'
            elif i.status == 3:
                status = u'放弃'
            else:
                status = u'未知'
            res.append({
                'id': i.id,
                'task': i.name,
                'desc': i.desc,
                'status': status,
                'create_time': str(i.create_time)
            })
        if res:
            return jsonify(res)
        else:
            return jsonify({'status': '404', 'msg': u'无数据'})


class del_list(Resource):

    def post(self):
        if request.form:
            json_data = [dict(request.form)[key] for key in dict(request.form)]
            data = [int(i) for i in json_data[0]]

            db.session.query(Todo).filter(
                Todo.id.in_(data)).delete(
                synchronize_session=False)
            db.session.commit()
            return jsonify({'code': '200'})
        else:
            return jsonify({'code': '500'})


class add_list(Resource):

    def post(self):
        try:
            json_data = {
                key: dict(
                    request.form)[key] for key in dict(
                    request.form)}
            task = json_data['task_name'][0]
            desc = json_data['task_desc'][0]
            status = json_data['task_status'][0]
            c_time = time.strftime('%Y-%m-%d %H:%M:%S')
            new_t = Todo(
                name=task,
                desc=desc,
                status=status,
                create_time=c_time)
            db.session.add(new_t)
            db.session.commit()
            return jsonify({'code': '200'})
        except Exception as e:
            print str(e)
            return jsonify({'code': '500'})


class edit_list(Resource):

    def post(self):
        json_data = {
            key: dict(
                request.form)[key] for key in dict(
                request.form)}
        task = json_data['task_name'][0]
        desc = json_data['task_desc'][0]
        task = u'{task}'.format(task=task)
        desc = u'{desc}'.format(desc=desc)
        if task and desc:
            id = json_data['task_id'][0]
            status = json_data['task_status'][0]
            c_time = time.strftime('%Y-%m-%d %H:%M:%S')
            db.session.query(Todo).filter(Todo.id == id).update(
                {'status': status, 'name': task, 'desc': desc, 'modify_time':c_time})
            db.session.commit()
            return jsonify({'code': '200'})
        else:
            return jsonify({'code': '500'})

api.add_resource(all_list, '/api/v1/all')
api.add_resource(add_list, '/api/v1/add')
api.add_resource(edit_list, '/api/v1/edit')
api.add_resource(del_list, '/api/v1/delete')
