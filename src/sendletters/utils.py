from accounts.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string

# TODO
'''
TODO надо сделать разные функции для а) сбора адресов по наниматель/работник
б) раздельной отправки в) выбора шаблонов почты
'''


def send_test_email():
    maillist = []
    for user in User.objects.all():
        maillist.append(user.email)
    for mail in maillist:
        subject = 'Тестовое письмо'
        # context = {
        # TODO собрать имена пользователей для контекста
        # }
        message = render_to_string('sendletters/email_templates/test_letter.txt')
        # TODO разобраться с сенд_масс_мейл
        send_mail(subject, message, 'anussebedernipes@yandex.ru', [mail])
