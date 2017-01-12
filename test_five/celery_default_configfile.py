
CELERY_IGNORE_RESULT = True
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True

CELERYD_POOL_RESTARTS = True
CELERYD_PREFETCH_MULTIPLIER=5

# 每个worker最多执行万100个任务就会被销毁，可防止内存泄露
CELERYD_MAX_TASKS_PER_CHILD=100
CELERY_ACCEPT_CONTENT = ['json']

# 单个任务的运行时间不超过此值，否则会被SIGKILL 信号杀死
CELERYD_TASK_TIME_LIMIT=3600 * 240

CELERY_TASK_SERIALIZER='json'
CELERY_TIMEZONE='Asia/Shanghai'
# CELERY_ENABLE_UTC=True

# CELERY_IMPORTS=("mongo2mysql")
# 任务发出后，经过一段时间还未收到acknowledge , 就将任务重新交给其他worker执行
CELERY_DISABLE_RATE_LIMITS = True
# 非常重要,有些情况下可以防止死锁
# CELERYD_FORCE_EXECV = True
# 某个程序中出现的队列，在broker中不存在，则立刻创建它
CELERY_CREATE_MISSING_QUEUES = True
# Enables error emails.
CELERY_SEND_TASK_ERROR_EMAILS = True
SEND_TASK_SENT_EVENT = True

BROKER_POOL_LIMIT = 10
BROKER_CONNECTION_MAX_RETRIES = 20

CELERY_REDIS_MAX_CONNECTIONS = 40


CELERY_QUEUES = {
    "first_queue": {
        "exchange": "first_queue",
        "exchange_type": "direct",
        "routing_key": "first_queue"
    },
    "first_queue2": {
        "exchange": "first_queue2",
        "exchange_type": "direct",
        "routing_key": "first_queue2"
    },
}

BROKER_TRANSPORT_OPTIONS = {
    'fanout_prefix': True,
    'visibility_timeout': 0
}



# RabbitMQ management api
persistent=True
# db="flower_db"
#broker="amqp://192.168.72.132:5672"
#broker_api="http://192.168.72.132:55672/api/"
logging="info"
