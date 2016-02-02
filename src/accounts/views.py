from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
import hashlib, random

from .forms import LoginForm, RegisterForm
from .models import User, UserActivationKey
from .utils import send_registration_email
# Create your views here.


def login_account_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        '''чтобы логиниться и по почте и по юзернейму
        нужен трай/эксепт проверяющий существование данных из поля
        в объектах класса Юзер(User.objects.get())почта или юзернейм
        '''
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # TODO вставить сообщение что успешно залогинился
                return redirect('main')
            else:
                pass # нужно активировать пользователя
        else:
            # TODO вставить сообщение что пользователя не существует
            # Вообще это неправильно делать такой принудительный редирект
            # возможно надо рейзить формеррор и давать ссылку на регистрацию
            return redirect('register')
    context = {
        "title": "Вход",
        "form": form
    }
    return render(request, 'accounts/login.html', context)


# TODO сообщение об успешной регистрации, сейчас после отправки формы ничего не происходит
def register_account_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        new_user = User.objects.create_user(username, email, password)
        new_user.is_active = False
        # TODO убрать в отдельную функцию
        # сгенерировать ключ для нового пользователя
        emailhash = email.encode('utf-8')
        salt_to_str_to_utf = str(random.random()).encode('utf-8')
        new_salt = hashlib.sha1(salt_to_str_to_utf).hexdigest()[:18]
        new_salt_to_utf = new_salt.encode('utf-8')
        key = hashlib.sha1(emailhash + new_salt_to_utf).hexdigest()
        UserActivationKey.objects.create(user=new_user, activation_key=key)
        new_user.save()
        # TODO убрать в отдельную функцию
        # отправить имейл для подтверждения активации
        send_registration_email(new_user, key)
    context = {
        "title": "Регистрация",
        "form": form,
    }
    return render(request, 'accounts/register.html', context)


def register_confirmation_view(request, activation_key):
    user_check_token = get_object_or_404(UserActivationKey, activation_key=activation_key)
    user = user_check_token.user
    user.is_active = True
    user.save()
    context = {
        "title": "Добро пожаловать!"
    }
    return render(request, 'accounts/registration_confirmed.html', context)


def logout_account_view(request):
    logout(request)
    # TODO вставить сообщение о разлогинивании
    return redirect('main')
