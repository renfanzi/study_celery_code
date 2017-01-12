#!/usr/bin/env python
# -*- coding:utf-8 -*-

# http://bbs.lampbrother.net/read-htm-tid-175873.html


"""

import requests
import time

def func(urls):
    start = time.time()
    for url in urls:
        resp = requests.get(url)
        print(resp.status_code)
    print("It took", time.time() - start, "seconds")

if __name__ == "__main__":
    func(["http://oneapm.com", "http://jd.com", "https://taobao.com", "http://baidu.com", "http://news.oneapm.com"])

"""

import requests
from celery import Celery

app = Celery('celery_blog', broker='amqp://192.168.72.132:5672')


@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(resp.status_code)


def func(urls):
    for url in urls:
        # fetch_url.delay(url)
        fetch_url(url)


if __name__ == "__main__":
    func(["http://www.jd.com", "https://www.taobao.com", "http://www.baidu.com"])





#celery worker -A celery_blog -l info -c 5 运行celery
