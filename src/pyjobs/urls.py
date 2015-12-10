from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from adverts import views

urlpatterns = [
    url(r'^$', views.AdvertList.as_view(), name='home'),
    url(r'^advert/(?P<pk>\d+)/$', views.AdvertDetail.as_view(), name='advert-detail'),
    url(r'^about/$', views.AboutUs.as_view(), name='about-us'),
    url(r'^conditions/$', views.Conditions.as_view(), name='conditions'),
    url(r'^registration/$', views.registration_view, name='registration'),
    url(r'author/add/$', views.advert_create, name='advert-add'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^userprofile/$', views.edit_user_profiles_view, name='profile'),
    url(r'^registersuccess/', views.RegisterSuccess.as_view(), name='register-success'),
    url(r'^registerlinkexpired/', views.RegistrationLinkExpired.as_view(), name='register-link-expired'),
    url(r'^confirm/(?P<activation_key>\w+)/$', views.register_confirmation, name='register-confirm'),
    url(r'^logout/$', views.logout_view, name='logout2'), #  для кастомизации нужно вызывать раньше, чем ауф.юрлс
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
