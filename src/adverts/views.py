from django.shortcuts import render
from django.views.generic import View, FormView, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from adverts import models


class AboutUs(TemplateView):
    template_name = 'adverts/about.html'


class AdvertList(ListView):
    model = models.Advert


class AdvertDetail(DetailView):
    model = models.Advert
