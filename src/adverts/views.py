from django.shortcuts import render, render_to_response
from django.views.generic import View, FormView, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import UserRegistrationForm, AdvertForm, UserLoginForm
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


class UserProfilesViews(TemplateView):
    template_name = 'adverts/userprofile.html'
