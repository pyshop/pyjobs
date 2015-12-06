from django.shortcuts import render, render_to_response
from django.views.generic import View, FormView, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import UserRegistrationForm, AdvertForm, UserLoginForm, EditUsersProfilesForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout  # its core of authentication and defaults models

from adverts import models


class AboutUs(TemplateView):
    template_name = 'adverts/about.html'


class AdvertList(ListView):
    model = models.Advert


class AdvertDetail(DetailView):
    model = models.Advert


class Conditions(TemplateView):
    template_name = 'adverts/conditions.html'


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
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        login(request, user)
        return HttpResponseRedirect(reverse('profile'))
    return render(request, 'adverts/registration.html', {'form': form})


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        login(request, user)
        return HttpResponseRedirect(reverse('profile'))
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def edit_user_profiles_view(request):
    user = request.user #пользователь для изменения = запросить пользователя
    form = EditUsersProfilesForm(request.POST or None) #форма из формс.пай
    if form.is_valid(): #если форма валидна
        user.first_name = request.POST['first_name'].strip() or user.first_name #first_name объекта юзер изменяется на то что поучаем в ПОСТ
        user.last_name = request.POST['last_name'].strip() or user.last_name #.strip() костыль для того, чтобы не перезаписывались пустые поля
        user.email = request.POST['email'].strip() or user.email
        user.phone = request.POST['phone'].strip() or user.phone
        user.save()
        return HttpResponseRedirect(reverse('profile'))
    return render(request, 'adverts/userprofile.html', {'form': form})
