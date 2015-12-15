from django.core.mail import send_mail
import hashlib, random
from .models import UserActivationKey

def create_hash_for_register_email(request, user):
    email = request.POST.get('email')
    email_utf = email.encode('utf-8')
    str_salt_utf = str(random.random()).encode('utf-8')
    salt = hashlib.sha1(str_salt_utf).hexdigest()[:5]  # can i use .enсode('utf-8')?
    salt_utf = salt.encode('utf-8')
    key = hashlib.sha1(email_utf + salt_utf).hexdigest()
    UserActivationKey.objects.create(user=user, activation_key=key)
    return key


def send_registration_email(user, key):
    subject = 'Подтверждение регистрации'
    message = "Привет %s, спасибо за регистрацию. Для того чтобы активировать аккаунт," \
                      " перейдите по этой ссылке: http://127.0.0.1:8010/confirm/%s" % (user.username, key)
    send_mail(subject, message, 'anussebedernipes@yandex.ru', [user.email], fail_silently= False)


