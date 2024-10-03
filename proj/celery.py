from celery import Celery
import sys
import platform

app = Celery('tasks', broker='redis://localhost:6379/0', result_backend='redis://')
if 'worker' in sys.argv:
    ping_result = app.control.ping()
    if len(ping_result) > 0 and f'celery@{platform.node()}' in ping_result[0]:
        print(f'Another worker is running')
        exit(1)    