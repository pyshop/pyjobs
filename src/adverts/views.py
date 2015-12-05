from django.shortcuts import render, render_to_response
from django.views.generic import View, FormView, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import UserRegistrationForm, AdvertForm, UserLoginForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login  # its core of authentication and defaults models

from adverts import models


class AboutUs(TemplateView):
    template_name = 'adverts/about.html'


class AdvertList(ListView):
    model = models.Advert


class AdvertDetail(DetailView):
    model = models.Advert


class Conditions(TemplateView):
    template_name = 'adverts/conditions.html'


# Comment this because we need to use new Form Based Views
# class Registration(CreateView):
#    template_name = 'adverts/registration.html'
#    model = models.UserRegistration
#    fields = ('username', 'password', 'email', 'phone')


# class AdvertCreate(CreateView):
#    model = models.Advert
#    fields = ('title', 'description', 'requirements', 'salary', 'city')

#    def form_valid(self, form):
#        if self.request.user.is_anonymous():
#            form.instance.author = None
#        else:
#            form.instance.author = self.request.user
#        return super(AdvertCreate, self).form_valid(form)


# class Login(CreateView):
#    template_name = 'registration/login.html'
#    model = models.UserLogin
#    fields = ('username', 'password')


def advert_create(request):
    form = AdvertForm(request.POST or None) # форма AdvertForm принимает запрос ПОСТ или None
    if form.is_valid():  # проверяется валидность формы "под капотом"
        form.save()  # форма сохраняется
        return HttpResponseRedirect(reverse('home'))  # в случае валидности формы функция возвращает страницу полученную reverse из urls.py 'home'
    return render(request, 'adverts/advert_form.html', {'form': form})  # рендерит страницу по указанному адресу?


def registration_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('conditions'))
    return render(request, 'adverts/registration.html', {'form': form})


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        login(request, user)
        return HttpResponseRedirect(reverse('conditions'))
    return render(request, 'registration/login.html', {'form': form})

# https://docs.djangoproject.com/en/1.8/topics/auth/default/#django.contrib.auth.login руководствовался этим
# def login_view(request):
#     username = request.POST['username'] #  берет значение по ключу 'username' из POST прочитал тут: http://djbook.ru/rel1.8/ref/request-response.html#django.http.HttpRequest.POST
#     password = request.POST['password']
#     user = authenticate(username=username, password=password) #  метод authenticate берет данные из формы? (по умолчанию логин и пароль) и передает в user
#     if user is not None: #  если user не пустой, а в каких случаях user будет None?
#         #проверить пароль/залогинить пользователя/распаковать/функция аутентификации и потом логин
#         if user.is_active(): # проверяет ли активен аккаунт, тоже под капотом http://djbook.ru/rel1.8/topics/auth/customizing.html?highlight=is_active#django.contrib.auth.is_active
#             login(request, user) # это тоже встроенная функция django.contrib.auth http://djbook.ru/rel1.8/topics/auth/default.html?highlight=login#django.contrib.auth.login
#             return HttpResponseRedirect(reverse('home')) # reverse возвращает нам страницу 'home' из urls.py
#         else:
#             return HttpResponseRedirect(reverse('home')) # здесь должен быть редирект на другую страницу, если пользователь неактивен
#     else:
#         return HttpResponseRedirect(reverse('home')) # здесь должен быть редирект на ошибку неправильный логин
# у нас ошибки ловятся {% if form.errors %} в шаблоне, а написанная мной функция не работает в строке 84
#
# What you actually have to do is create a custom authentication backend
#  вторая попытка сделать вьюху для логина http://djbook.ru/examples/19/ используется этот пример
# def login_view(request):
#     form = UserLoginForm(request.POST or None) #используется форма импортированная из файла forms.py
#     if form.is_valid():
#         username = form.cleaned_data.get('username')  #подробнее о методе get https://docs.djangoproject.com/en/1.8/topics/db/queries/#retrieving-a-single-object-with-get
#         password = form.cleaned_data.get('password')
#         user = auth.authenticate(username=username, password=password) # описал в предыдущей форме
#         if user.is_active():
#             auth.login(request, user)
#             return HttpResponseRedirect(reverse('home'))
#         # else:
#             # return HttpResponseRedirect(reverse('user-inactive'))
#     #else:
#        # return HttpResponseRedirect(reverse('registration-errors'))
#     else:
#         return render(request, 'adverts/login.html', {'form': form})
