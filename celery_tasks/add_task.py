from celery import Celery
import time

app = Celery('add_task',broker='amqp://guest:guest@rabbitmq:5672//',backend='rpc://')

@app.task()
def ten_seconds_add(x,y):
    time.sleep(10)
    return x + y