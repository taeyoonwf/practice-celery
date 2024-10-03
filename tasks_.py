from celery import Celery, current_task
import threading
import time

app = Celery('tasks', broker='redis://localhost:6379/0'
             , result_backend='redis://'
            )

@app.task
def add(x, y):
    #print(current_task.request.id)
    #time.sleep(10)
    s = 0
    thread_code = int(threading.current_thread().name[-1])
    for i in range(100):
        for j in range(100):
            for k in range(100):
                for q in range(100):
                    s += thread_code + 1 + i + j + k
    print(f'The name of the current thread is {threading.current_thread().name}.')
    return x + y + s
