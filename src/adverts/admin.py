from django.contrib import admin

from adverts import models

admin.site.register(models.User)
admin.site.register(models.Advert)
