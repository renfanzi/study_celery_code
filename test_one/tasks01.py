#!/usr/bin/env python
# -*- coding:utf-8 -*-



from test_one.celery01 import celery


@celery.task()
def ddd(my_id):
    print("ddddddd")

    return 'ok%s' % my_id
