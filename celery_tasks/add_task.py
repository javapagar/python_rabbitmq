from celery import Celery
import time

app = Celery('celery_tasks.add_task',broker='amqp://guest:guest@localhost:5672//',backend='rpc://')

@app.task
def add(x,y):
    time.sleep(10)
    return x + y