from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import password_reset_confirm
from django.contrib import messages
from .utils import generate_activation_key


# import hashlib
# import random

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
                messages.success(request, "Привет %s!" % user.username)
                return redirect('main')
            else:
                messages.warning(request, "Кажется вы забыли активировать аккаунт!")
                return redirect('login')
        else:
            messages.warning(request, "Кажется что-то пошло не так! Попробуйте еще раз.")
            return redirect('login') # TODO надо научиться передавать контекст в случае какого-либо условия
            # то есть если пользователя не существует, то рендерится шаблон 'login', но уже с ссылкой на регистрацию
    context = {
        "title": "Вход",
        "form": form
    }
    return render(request, 'accounts/login.html', context)


def register_account_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        new_user = User.objects.create_user(username, email, password, slug=username)
        new_user.is_active = False
        key = generate_activation_key(email)
        UserActivationKey.objects.create(user=new_user, activation_key=key)
        new_user.save()
        send_registration_email(new_user, key)
        messages.success(request, "Регистрация прошла успешно, ссылка для активации "
                                  "отправлена на указанную электропочту!")
        return redirect('main')
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
    messages.success(request, "Вы больше не залогинены")
    return redirect('main')


