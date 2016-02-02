from django.contrib import admin
from .models import SubscriptionSignUp


# Register your models here.
class SubscriptionSignUpAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'is_worker', 'is_recruiter', 'timestamp']

    class Meta:
        model = SubscriptionSignUp


admin.site.register(SubscriptionSignUp, SubscriptionSignUpAdmin)
