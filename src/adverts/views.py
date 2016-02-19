from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
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
    queryset = Advert.objects.order_by('-timestamp')
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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AdvertsCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class AdvertsUpdateView(UpdateView):
    model = Advert
    fields = ['title', 'description', 'requirements', 'salary', 'city', 'is_remote']
    success_url = '/adverts/'
    template_name = 'adverts/advert_create.html'

    def get_object(self, queryset=None):
        advert = super(AdvertsUpdateView, self).get_object()
        if advert.author != self.request.user:
            raise PermissionDenied()
        return advert


class AdvertsDeleteView(DeleteView):
    model = Advert
    success_url = '/adverts/'
