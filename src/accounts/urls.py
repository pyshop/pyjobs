from django.conf.urls import url


from accounts import views

urlpatterns = [
    url(r'^login/$', views.login_account_view, name='login'),
    url(r'^logout/$', views.logout_account_view, name='logout'),
    url(r'^register/$', views.register_account_view, name='register'),
    url(r'^confirm/(?P<activation_key>\w+)/$', views.register_confirmation_view, name='confirmed'),
    # url(r'^create/$', views.adverts_create_view, name='advert_create'),
    # url(r'^(?P<id>\d+)/edit/$', views.adverts_update_view, name='advert_update'),
    # url(r'^(?P<id>\d+)/delete/$', views.adverts_delete_view),
]
