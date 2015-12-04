from django import forms
from django.shortcuts import render, render_to_response
from django.views.generic import View, FormView, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .forms import UserRegistrationForm, AdvertForm, UserLoginForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

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

#
def advert_create(request):
    if request.method == 'POST':
        form = AdvertForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            pass
    else:
        form = AdvertForm()
    return render(request, 'adverts/advert_form.html', {'form': form})


def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('conditions'))
        else:
            pass
    else:
        form = UserRegistrationForm()
    return render(request, 'adverts/registration.html', {'form': form})


def login_view(request):
    form = UserLoginForm()
    if form.is_valid():
        return render(request, '/', {})
    else:
        return render(request, 'login', {})
