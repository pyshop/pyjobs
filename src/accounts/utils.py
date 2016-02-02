from django.core.mail import send_mail
from django.template.loader import render_to_string
from pyjobs2.settings import DEFAULT_FROM_EMAIL


def send_registration_email(user, key):
    context = {
        'user': user.username,
        'key': key,
    }
    message = render_to_string('accounts/email_templates/registration_email.txt', context)
    subject = render_to_string('accounts/email_templates/registration_subject.txt')
    from_email = DEFAULT_FROM_EMAIL
    to_email = user.email
    send_mail(subject, message, from_email, [to_email], fail_silently=False)
