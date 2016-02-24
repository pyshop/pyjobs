from accounts.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )


class UserProfileDetails(DetailView):
    model = User
    template_name = 'profiles/user_profile.html'
    context_object_name = 'user_profile'
    


class UserProfileUpdate(UpdateView):
    model = User
    fields = ['location', 'phone', 'is_worker', 'is_recruiter', 'homepage', 'email_to_contact']
    template_name = 'profiles/user_profile_update.html'
    success_url = '/profiles/{slug}/'

    def get_object(self, queryset=None):
        profile = super(UserProfileUpdate, self).get_object()
        if profile.username != self.request.user.username:
            raise PermissionDenied()
        return profile

    # def get_success_url(self):
    #     return redirect('profile', kwargs={'slug': 'request.user.username'})
