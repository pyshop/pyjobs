from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.


def send_contact_email_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        messages.success(request, "Сообщение отправлено!")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        name = form.cleaned_data.get("name")
        contact_message = """
        %s: %s via %s
        """ % (name, message, email)
        send_mail(subject, contact_message, settings.DEFAULT_FROM_EMAIL,
                    ['orekhovo.textile@gmail.com'], fail_silently=False)

    context = {
        "form": form,
        "title": "Контакты"
    }
    return render(request, 'sendletters/contact.html', context)