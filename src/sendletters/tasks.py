# from celery import Celery
from pyjobs2.celery import app
from sendletters.utils import test_send_mass_to_users

# app = Celery('tasks', broker='redis://localhost:6379/0')


# @app.task(name='testtask')
# def send_and_print():
#     send_test_email()
#     print("Print and may be sent")

@app.task(name='mass_to_users')
def send_and_print():
    test_send_mass_to_users()
    print("Print and may be sent")
