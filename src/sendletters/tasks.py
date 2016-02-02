# from celery import Celery
from pyjobs2.celery import app
from sendletters.utils import send_test_email

# app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task(name='testtask')
def send_and_print():
    send_test_email()
    print("Print and may be sent")
