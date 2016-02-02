from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Advert
from .forms import AdvertCreateForm
# Create your views here.


def adverts_list_view(request):
    queryset = Advert.objects.all().order_by("-timestamp")
    context = {
        "objects_list": queryset,
        "title": "Все объявления",
    }
    return render(request, 'adverts/adverts_list.html', context)


def adverts_details_view(request, id):
    instance = get_object_or_404(Advert, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, 'adverts/advert_detail.html', context)


def adverts_create_view(request):
    form = AdvertCreateForm(request.POST or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.save()
        messages.success(request, "Объявление опубликовано")
        return redirect('adverts')
    else:
        messages.error(request, "Ошибка формы")
    context = {
        "title": "Новое объявление:",
        "form": form
    }
    return render(request, 'adverts/advert_create.html', context)


def adverts_update_view(request, id):
    instance = get_object_or_404(Advert, id=id)
    form = AdvertCreateForm(request.POST or None, instance=instance)
    if form.is_valid():
        data = form.save(commit=False)
        data.save()
        messages.success(request, "Объявление обновлено")
        return redirect('adverts')
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, 'adverts/advert_create.html', context)


def adverts_delete_view(request, id):
    instance = get_object_or_404(Advert, id=id)
    instance.delete()
    messages.success(request, "Объявление удалено")
    return redirect('adverts')