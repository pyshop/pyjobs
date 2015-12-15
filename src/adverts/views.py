from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views.generic import View, FormView, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import UserRegistrationForm, AdvertForm, UserLoginForm, EditUserProfileForm
from .models import User, UserActivationKey
from .utils import send_registration_email, create_hash_for_register_email
from django.contrib.auth import authenticate, login, logout
from django import forms

from adverts import models


class AboutUs(TemplateView):
    template_name = 'adverts/about.html'


class AdvertList(ListView):
    model = models.Advert


class AdvertDetail(DetailView):
    model = models.Advert


class Conditions(TemplateView):
    template_name = 'adverts/conditions.html'


class RegisterSuccess(TemplateView):
    template_name = 'adverts/registration_success.html'


class RegistrationLinkExpired(TemplateView):
    template_name = 'adverts/registration_link_expired.html'


def advert_create(request):
    form = AdvertForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'adverts/advert_form.html', {'form': form})


def registration_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        key = create_hash_for_register_email(request, user)
        user.save()
        send_registration_email(user, key)
        return redirect('register-success')
    return render(request, 'adverts/registration.html', {'form': form})


def register_confirmation(request, activation_key):
    if request.user.is_authenticated():
        return redirect('home')
    user_check_token = get_object_or_404(UserActivationKey, activation_key=activation_key)
    # if user_profile.key_expires < datetime.datetime.now():
    #     return render_to_response('adverts/registration_link_expired.html')
    user = user_check_token.user
    user.is_active = True
    user.save()
    return render_to_response('adverts/registration_email_confirmed.html')


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('profile')
            else:
                return redirect('profile')
        else:
            return redirect('profile') # TODO надо не редирект, а указатель с ошибкой на той же странице
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def edit_user_profiles_view(request):
    user = request.user
    form = EditUserProfileForm(request.POST or None)
    if form.is_valid():
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.phone = request.POST['phone']
        user.save()
        return redirect('profile')
    return render(request, 'adverts/userprofile.html', {'form': form})

