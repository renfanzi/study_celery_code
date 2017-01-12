#!/usr/bin/env python
# -*- coding:utf-8 -*-


from celery import Celery

app = Celery('celery_config', broker='amqp://192.168.72.132:5672', include=['celery_blog', 'celery_add'])

