from django.conf.urls import url
from .views import UserProfileDetails, UserProfileUpdate

urlpatterns = [
    url(r'^(?P<slug>[\w.@+-]+)/$', UserProfileDetails.as_view(), name='profile'),
    url(r'^(?P<slug>[\w.@+-]+)/edit/$', UserProfileUpdate.as_view(), name='profile_update'),
]
