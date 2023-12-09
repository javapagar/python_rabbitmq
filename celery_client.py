from celery_tasks.add_task import add

if __name__ == "__main__":
    for i in range(6):
        add.delay(4,i)