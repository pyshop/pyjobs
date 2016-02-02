"""pyjobs2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from pyjobs2 import views
from sendletters.views import send_contact_email_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.main_page_view, name='main'),
    url(r'^adverts/', include("adverts.urls")),
    url(r'^accounts/', include("accounts.urls")),
    url(r'^contact/', send_contact_email_view, name='contact')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
