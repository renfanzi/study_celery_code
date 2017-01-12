#!/usr/bin/env python
# -*- coding:utf-8 -*-

#http://docs.jinkan.org/docs/celery/configuration.html#configuration
# 代理设置
BROKER_URL = 'amqp://'

# celery 开始时要导入的模块列表
CELERY_IMPORTS = ('')

#使用数据库来存储任务状态和结果
CELERY_RESULT_BACKEND = 'amqp://'

#CELERY_ANNOTATIONS  =  { "tasks.add": { "rate_limit" : '10 / S' }}


#CELERYD_CONCURRENCY = 20  # 并发worker数

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

#使用串行名（不懂）
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Europe/Oslo'

# 设置时间
#CELERY_ENABLE_UTC = True
#CELERY_TIMEZONE = 'ASIA/shanghai'


#设置CPU的并发
# CELERY_CONCURRENCY = 4
#CELERYD_PERFETCH_MYLTIPLIER = 4

#数据库url例子
#CELERY_RESULT_BACKEND  =  'DB +计划：//用户名：密码@主机：端口/ DBNAME“
# ＃mysql CELERY_RESULT_BACKEND ='db + mysql：// scott：tiger @ localhost / foo'

"""
celery = Celery(
    'com.analysis.tasks.data_analysis',
    broker='amqp://42.62.6.220:5672',
    include='com.analysis.tasks.data_analysis'
)
celery.conf.CELERY_RESULT_BACKEND = "amqp://42.62.6.220:5672"
celery.conf.CELERY_ACCEPT_CONTENT = ['application/json']
celery.conf.CELERY_TASK_SERIALIZER = 'json'
celery.conf.CELERY_RESULT_SERIALIZER = 'json'
#定义心跳
celery.conf.BROKER_HEARTBEAT = 30

celery.conf.CELERY_IGNORE_RESULT = False  # this is less important
"""




