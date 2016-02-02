from django.conf.urls import url


from adverts import views

urlpatterns = [
    url(r'^$', views.adverts_list_view, name='adverts'),
    url(r'^(?P<id>\d+)/$', views.adverts_details_view, name='advert_detail'),
    url(r'^create/$', views.adverts_create_view, name='advert_create'),
    url(r'^(?P<id>\d+)/edit/$', views.adverts_update_view, name='advert_update'),
    url(r'^(?P<id>\d+)/delete/$', views.adverts_delete_view),
]
