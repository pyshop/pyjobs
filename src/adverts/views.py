from django.shortcuts import render
from django.views.generic import View, FormView, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from adverts import models


class AboutUs(TemplateView):
    template_name = 'adverts/about.html'


class AdvertList(ListView):
    model = models.Advert


class AdvertDetail(DetailView):
    model = models.Advert


class Conditions(TemplateView):
    template_name = 'adverts/conditions.html'


class Registration(TemplateView):
    template_name = 'adverts/registration.html'


class AdvertCreate(CreateView):
    model = models.Advert
    fields = ('title', 'description', 'requirements', 'salary', 'city')

    def form_valid(self, form):
        if self.request.user.is_anonymous():
            form.instance.author = None
        else:
            form.instance.author = self.request.user
        return super(AdvertCreate, self).form_valid(form)


class Login(TemplateView):
    template_name = 'registration/login.html'