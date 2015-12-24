from celery.task import periodic_task  # декораторы теперь следует импортировать из celery.task
from mailer.engine import send_all
from datetime import timedelta

# this will run every 60 seconds
# send all emails in the mailer queue


@periodic_task(run_every=timedelta(seconds=60))
def email_tasks():
    send_all()
