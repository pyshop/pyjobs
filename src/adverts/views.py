from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )


from .models import Advert


class AdvertsListView(ListView):
    model = Advert
    template_name = 'adverts/adverts_list.html'
    paginate_by = 10
    context_object_name = 'objects_list'


class AdvertsDetailView(DetailView):
    model = Advert
    template_name = 'adverts/advert_detail.html'


class AdvertsCreateView(SuccessMessageMixin, CreateView):
    model = Advert
    fields = ['title', 'description', 'requirements', 'salary', 'city', 'is_remote']
    success_url = '/adverts/'
    template_name = 'adverts/advert_create.html'
    success_message = "Объявление опубликовано"


class AdvertsUpdateView(UpdateView):
    model = Advert
    fields = ['title', 'description', 'requirements', 'salary', 'city', 'is_remote']
    success_url = '/adverts/'
    template_name = 'adverts/advert_create.html'


class AdvertsDeleteView(DeleteView):
    model = Advert
    success_url = '/adverts/'
