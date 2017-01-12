#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 将 celery 代码和配置保存在不同文件中


import requests
from celery_base import app


def test_file():
    with open("a.txt", 'w', encoding='utf-8') as f:
        f.write("hello,hello, hello")


@app.task
def fetch_url(url):
    resp = requests.get(url)
    test_file()
    return "hello world"

