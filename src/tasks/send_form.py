from src.celery_app import app



@app.task(name='task1')
def task_1():
    return 'this is a success task'
