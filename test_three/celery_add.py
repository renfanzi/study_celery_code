#!/usr/bin/env python
# -*- coding:utf-8 -*-

from celery_config import app


@app.task
def add(a, b):
    return a + b