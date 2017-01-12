#!/usr/bin/env python
# -*- coding:utf-8 -*-


from celery_base import app


def test():
    urls = "http://www.jd.com"

    ret = app.send_task('celery_tasks.fetch_url', args=[urls], queue='first_queue')
    print(ret)


test()



# celery 启动命令celery worker -A celery_tasks -l info -c 5



# celery.send_task("ct.ctask.pid_action_task", args=[pid, limit, skip], queue="first_ct_queue2")
