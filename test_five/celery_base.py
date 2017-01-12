#!/usr/bin/env python
# -*- coding:utf-8 -*-


from celery import Celery

#app = Celery("这个文件名"， boker， include【放tasks的文件， 文件2】)

app = Celery('celery_base', broker='amqp://192.168.72.132:5672', include=['celery_tasks'])

app.config_from_object('celery_default_configfile')