#!/usr/bin/env python
# -*- coding:utf-8 -*-


from celery import Celery

app = Celery('celery_config', broker='amqp://192.168.72.132:5672', include=['celery_blog'])

app.conf.update(
    CELERY_ROUTES = {
        "first_queue": {
            "exchange": "first_queue",
            "exchange_type": "direct",
            "routing_key": "first_queue"
        },
    }
)



"""
CELERY_QUEUES = {
    "first_ct_queue": {
        "exchange": "first_ct_queue",
        "exchange_type": "direct",
        "routing_key": "first_ct_queue"
    },
    "first_ct_queue2": {
        "exchange": "first_ct_queue2",
        "exchange_type": "direct",
        "routing_key": "first_ct_queue2"
    },
}

"""