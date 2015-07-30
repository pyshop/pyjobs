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
    url(r'^registration/$', views.Registration.as_view(), name='registration'),
    url(r'author/add/$', views.AdvertCreate.as_view(), name='advert-add'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
