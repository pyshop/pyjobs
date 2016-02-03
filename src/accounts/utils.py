from django.core.mail import send_mail
from django.template.loader import render_to_string
from pyjobs2.settings import DEFAULT_FROM_EMAIL

import hashlib
import random


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


def generate_activation_key(new_user):
        emailhash = new_user.email.encode('utf-8')
        salt_to_str_to_utf = str(random.random()).encode('utf-8')
        new_salt = hashlib.sha1(salt_to_str_to_utf).hexdigest()[:18]
        new_salt_to_utf = new_salt.encode('utf-8')
        key = hashlib.sha1(emailhash + new_salt_to_utf).hexdigest()
        return key
