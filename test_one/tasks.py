#!/usr/bin/env python
# -*- coding:utf-8 -*-

from celery import Celery

app = Celery('tasks', broker='amqp://192.168.72.132:5672')


@app.task
def add(x, y):
    return x + y


#运行celery -A tasks worker --loglevel=info
