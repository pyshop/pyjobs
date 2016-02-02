from django.contrib import admin

# Register your models here.
from .models import Advert


class AdvertModelAdmin(admin.ModelAdmin):
    list_display = ["title", "city", "salary", "is_remote", "timestamp"]
    search_fields = ["title", "city", "salary", "is_remote", "timestamp"]
    # поиск почему-то кейс-сенситив

    class Meta:
        model = Advert


admin.site.register(Advert, AdvertModelAdmin)
