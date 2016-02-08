from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import UserProfile
User = get_user_model()
# Create your views here.


def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = UserProfile.objects.get_or_create(user=user)
    context = {
        "profile": profile
    }
    return render(request, 'profiles/user_profile.html', context)
