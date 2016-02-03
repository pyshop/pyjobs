from django.conf.urls import url

# from adverts import views
from adverts.views import (
    AdvertsListView,
    AdvertsDetailView,
    AdvertsCreateView,
    AdvertsUpdateView,
    AdvertsDeleteView,
    )

urlpatterns = [
    # url(r'^$', views.adverts_list_view, name='adverts'),
    url(r'^$', AdvertsListView.as_view(), name='adverts'),
    # url(r'^(?P<id>\d+)/$', views.adverts_details_view, name='advert_detail'),
    url(r'^(?P<pk>\d+)/$', AdvertsDetailView.as_view(), name='advert_detail'),
    # url(r'^create/$', views.adverts_create_view, name='advert_create'),
    url(r'^create/$', AdvertsCreateView.as_view(), name='advert_create'),
    # url(r'^(?P<id>\d+)/edit/$', views.adverts_update_view, name='advert_update'),
    url(r'^(?P<pk>\d+)/edit/$', AdvertsUpdateView.as_view(), name='advert_update'),
    url(r'^(?P<pk>\d+)/delete/$', AdvertsDeleteView.as_view()),
]
