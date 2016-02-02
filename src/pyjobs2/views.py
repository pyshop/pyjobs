from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from sendletters.forms import SubscriptionSignUpForm
from accounts.models import User


def main_page_view(request):
    # надо вынести форму в отдельную функцию и убрать ее в /sendletters/views
    form = SubscriptionSignUpForm(request.POST or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.save()
        messages.success(request, "Подписка оформлена. Никакого спама, честно!")
        return redirect('main')
    # else:
    #     messages.error(request, "Подписка не оформлена")
    # постоянно висит это сообщение, я так понимаю проблема в темплейт-теге
    context = {
        "title": "PyJobs",
        "form": form,
    }
    return render(request, 'main.html', context)
