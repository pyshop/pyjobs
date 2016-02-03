from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )


from .models import Advert
from .forms import AdvertCreateForm
# Create your views here.


class AdvertsListView(ListView):
    model = Advert
    template_name = 'adverts/adverts_list.html'

    def get_context_data(self, **kwargs):
        context = super(AdvertsListView, self).get_context_data(**kwargs)
        context["objects_list"] = Advert.objects.all().order_by("-timestamp")
        context["title"] = "Все объявления"
        return context


# def adverts_list_view(request):
#     queryset = Advert.objects.all().order_by("-timestamp")
#     context = {
#         "objects_list": queryset,
#         "title": "Все объявления",
#     }
#     return render(request, 'adverts/adverts_list.html', context)


class AdvertsDetailView(DetailView):
    model = Advert
    template_name = 'adverts/advert_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AdvertsDetailView, self).get_context_data(**kwargs)
        context["title"] = "Все объявления"
        return context


# def adverts_details_view(request, id):
#     instance = get_object_or_404(Advert, id=id)
#     context = {
#         "title": instance.title,
#         "instance": instance,
#     }
#     return render(request, 'adverts/advert_detail.html', context)


class AdvertsCreateView(CreateView):
    model = Advert
    fields = ['title', 'description', 'requirements', 'salary', 'city', 'is_remote']
    success_url = '/adverts/'
    template_name = 'adverts/advert_create.html'

    def get_context_data(self, **kwargs):
        context = super(AdvertsCreateView, self).get_context_data(**kwargs)
        context["title"] = "Новое объявление"
        return context

# def adverts_create_view(request):
#     form = AdvertCreateForm(request.POST or None)
#     if form.is_valid():
#         data = form.save(commit=False)
#         data.save()
#         messages.success(request, "Объявление опубликовано")
#         return redirect('adverts')
#     else:
#         messages.error(request, "Ошибка формы")
#     context = {
#         "title": "Новое объявление:",
#         "form": form
#     }
#     return render(request, 'adverts/advert_create.html', context)


class AdvertsUpdateView(UpdateView):
    model = Advert
    fields = ['title', 'description', 'requirements', 'salary', 'city', 'is_remote']
    success_url = '/adverts/'
    template_name = 'adverts/advert_create.html'

    def get_context_data(self, **kwargs):
        context = super(AdvertsUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Обновить объявление"
        return context


# def adverts_update_view(request, id):
#     instance = get_object_or_404(Advert, id=id)
#     form = AdvertCreateForm(request.POST or None, instance=instance)
#     if form.is_valid():
#         data = form.save(commit=False)
#         data.save()
#         messages.success(request, "Объявление обновлено")
#         return redirect('adverts')
#     context = {
#         "title": instance.title,
#         "instance": instance,
#         "form": form,
#     }
#     return render(request, 'adverts/advert_create.html', context)


class AdvertsDeleteView(DeleteView):
    model = Advert
    success_url = '/adverts/'

# def adverts_delete_view(request, id):
#     instance = get_object_or_404(Advert, id=id)
#     instance.delete()
#     messages.success(request, "Объявление удалено")
#     return redirect('adverts')
