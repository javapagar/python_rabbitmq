FROM python:3.11.6-slim

COPY requirements.txt /
RUN pip install -r /requirements.txt

ADD . /celery_tasks
WORKDIR /celery_tasks

ENTRYPOINT celery -A add_task worker --loglevel=info