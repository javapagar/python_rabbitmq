from fastapi import FastAPI
from celery import Celery


app = FastAPI()
celery_app = Celery('celery_tasks',broker='amqp://guest:guest@rabbitmq:5672//',backend='rpc://')

@app.get("/health")
def health():
    return {"health":"All it's OK"}

@app.get("/tasks/add")
def health(number1:int,number2:int):
    result = celery_app.send_task('add_task.ten_seconds_add', kwargs={'x':number1,'y':number2})
    print(result.backend)
    return {"task_id":result.id}

@app.get("/tasks/{task_id}")
def health(task_id:str):
    result = celery_app.AsyncResult(task_id, app=celery_app)
    print(result.backend)
    return {"task_id":result.id,
            "state":result.state,
            "add_result":result.result}