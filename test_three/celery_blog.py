#!/usr/bin/env python
# -*- coding:utf-8 -*-

#将 celery 代码和配置保存在不同文件中


import requests
from test_three.celery_config import app
from test_three.celery_add import add

@app.task
def fetch_url(url):
     resp = requests.get(url)
     print(resp.status_code)

def func(urls):
    for url in urls:
       fetch_url(url)

if __name__ == "__main__":
    ret = add(2, 4)
    print(ret)
    func(["http://www.jd.com", "https://www.taobao.com", "http://www.baidu.com"])