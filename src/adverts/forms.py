from django import forms


from .models import Advert


class AdvertCreateForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ["title", "description", "requirements", "city", "salary", "is_remote"]
