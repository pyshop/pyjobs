from django.conf.urls import url
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)

from accounts import views

urlpatterns = [
    url(r'^login/$', views.login_account_view, name='login'),
    url(r'^logout/$', views.logout_account_view, name='logout'),
    url(r'^register/$', views.register_account_view, name='register'),
    url(r'^confirm/(?P<activation_key>\w+)/$', views.register_confirmation_view, name='confirmed'),
    url(r'^password_reset/$', password_reset, {'template_name': 'accounts/password_reset/password_reset_form.html'},
        name='password_reset'),
    url(r'^password_reset_done/$', password_reset_done,
        {'template_name': 'accounts/password_reset/password_reset_link_sent.html'}, name='password_reset_done'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'accounts/password_reset/password_reset_confirmed.html'}, name='password_reset_confirm'),
    url(r'^password_reset_complete/$', password_reset_complete,
        {'template_name': 'accounts/password_reset/password_reset_complete.html'}, name='password_reset_complete'),
]
