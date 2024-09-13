from celery import Celery
import threading
import time
from importlib import import_module
import sys
import os
import platform

sys.path.append('.')
app = Celery('tasks', broker='redis://localhost:6379/0', result_backend='redis://')

ping_result = app.control.ping()
if 'worker' in sys.argv and len(ping_result) > 0 and f'celery@{platform.node()}' in ping_result[0]:
    print(f'Another worker is running')
    exit(1)
    

@app.task
def add(x, y):
    #print(current_task.request.id)
    #time.sleep(10)
    s = 0
    thread_code = int(threading.current_thread().name[-1])
    for i in range(50):
        for j in range(50):
            for k in range(50):
                for q in range(50):
                    s += thread_code + 1 + i + j + k
    print(f'The name of the current thread is {threading.current_thread().name}.')
    return x + y + s


@app.task
def run_new_code(file_name, task_id):
    try:
        os.system('git pull')
    except:
        print('git pull error')
    if file_name in sys.modules:
        del sys.modules[file_name]
    new_code = import_module(file_name)
    return new_code.main(task_id)


@app.task
def celery_is_alive():
    print(app.control.inspect())
    print(app.control.ping())
    print(app.control.inspect().registered())
    #print(inspect().registered())
    return True


@app.task
def update_worker():
    try:
        os.system('git pull')
    except:
        print('git pull error')
    os.system('celery --app tasks worker --concurrency 8 --pool threads --loglevel=INFO')
    exit(0)