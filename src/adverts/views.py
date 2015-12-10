from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views.generic import View, FormView, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import UserRegistrationForm, AdvertForm, UserLoginForm, EditUserProfileForm
from .models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
import hashlib, datetime, random

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
        return redirect(reverse('home'))
    return render(request, 'adverts/advert_form.html', {'form': form})


def registration_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        email_utf = email.encode('utf-8')
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        salt_utf = salt.encode('utf-8')
        user = form.save()
        user.activation_key = hashlib.sha1(email_utf + salt_utf).hexdigest()
        #user.key_expires = datetime.datetime.today() + datetime.timedelta(hours=2)
        user.save()
        email_subject = 'Подтверждение регистрации'
        email_body = "Привет %s, спасибо за регистрацию. Для того чтобы активировать аккаунт," \
                     " перейдите по этой ссылке: http://127.0.0.1:8010/confirm/%s" % (username, user.activation_key)
        send_mail(email_subject, email_body, 'anussebedernipes@yandex.ru',
                        [email], fail_silently=False)
        return redirect(reverse('register-success'))
    return render(request, 'adverts/registration.html', {'form': form})


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user.is_active:
            login(request, user)
            return redirect(reverse('profile'))
        else:
            return redirect(reverse('profile'))
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


def edit_user_profiles_view(request):
    user = request.user
    form = EditUserProfileForm(request.POST or None)
    if form.is_valid():
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.phone = request.POST['phone']
        user.save()
        return redirect(reverse('profile'))
    return render(request, 'adverts/userprofile.html', {'form': form})


def register_confirmation(request, activation_key):
    if request.user.is_authenticated():
        return redirect(reverse('home'))
    user_check_token = get_object_or_404(User, activation_key=activation_key)
    # if user_profile.key_expires < datetime.datetime.now():
    #     return render_to_response('adverts/registration_link_expired.html')
    user = user_check_token
    user.is_active = True
    user.save()
    return render_to_response('adverts/registration_email_confirmed.html')
