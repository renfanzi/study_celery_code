#!/usr/bin/env python
# -*- coding:utf-8 -*-


from celery_config import app

def test():
    urls = ["http://www.jd.com", "https://www.taobao.com", "http://www.baidu.com"]

    app.send_task('celery_blog.fetch_url', args=[urls], queue ='first_queue')



test()



#celery 启动命令celery worker -A celery_blog -l info -c 5 



# celery.send_task("ct.ctask.pid_action_task", args=[pid, limit, skip], queue="first_ct_queue2")

