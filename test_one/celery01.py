#!/usr/bin/env python
# -*- coding:utf-8 -*-

""""""
from celery import Celery, platforms



celery = Celery("my_celery.test_one",
                # broker=app.config['CELERY_BROKER_URL'],
                broker='amqp://192.168.72.132:5672',
                include=['test_one.tasks01']
                )

celery.config_from_object("celeryconfig2.py")
platforms.C_FORCE_ROOT = True



my_id = "dsf"


def pid_action(my_id):
    celery.send_task("test_one.tasks01.ddd", args=[my_id], queue="first_ct_queue2")



