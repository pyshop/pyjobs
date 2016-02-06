from accounts.models import User
from django.core.mail import send_mail, send_mass_mail
from django.template.loader import render_to_string
from django.conf import settings

# TODO раздельные функции
'''
TODO надо сделать разные функции для а) сбора адресов по наниматель/работник
б) раздельной отправки в) выбора шаблонов почты
'''


def send_email(subject, message, email):
    return send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

#
# def send_password_reset_link_to_user(email, token_generator):
#     context = {
#         "email": email,
#         "token": token_generator,
#     }
#     subject = render_to_string('accounts/email_templates/password_reset_email_subject.txt')
#     message = render_to_string('accounts/email_templates/password_reset_email_message.txt', context)
#     to_email = email
#     send_email(subject, message, to_email)

# def send_test_email():
#     maillist = {}
#     for user in User.objects.all():
#         maillist[user.username] = user.email
#     for username, email in maillist.items():
#         subject = 'Тестовое письмо'
#         context = {
#             "user": username,
#         }
#         message = render_to_string('sendletters/email_templates/test_letter.txt', context)
#         from_mail = settings.DEFAULT_FROM_EMAIL
#         send_mail(subject, message, from_mail, [email])


def test_send_email_to_user(user):
    context = {
        "user": user.username
    }
    subject = render_to_string('sendletters/email_templates/test_letter_subject.txt')
    message = render_to_string('sendletters/email_templates/test_letter.txt', context)
    to_email = user.email
    send_email(subject, message, to_email)


# def send_mass_email(subject, message, recipient_list):
#     datatuple = ((subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list), )
#     return send_mass_mail(datatuple)


def test_send_mass_to_users():
    recipient_list = []
    for user in User.objects.all():
        recipient_list.append(user.email)
        context = {
            "user": user.username
        }
        subject = render_to_string('sendletters/email_templates/test_letter_subject.txt')
        message = render_to_string('sendletters/email_templates/test_letter.txt', context)
        # send_mass_email(subject, message, recipient_list)
        atuple = (subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
        datatuple = (atuple, )
        send_mass_mail(datatuple)
