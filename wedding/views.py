import json

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import GuestsForm
from .models import Guests


def home(request):
    rsvp_flag = False
    form = GuestsForm()
    if request.method == "POST":
        form = GuestsForm(request.POST)
        if form.is_valid():
            guest = Guests.objects.create(**form.cleaned_data)
            guest.save()
            # send_mail(
            #     "Neue Anmeldung Hochzeit",
            #     json.dumps(form.cleaned_data, indent=4),
            #     settings.EMAIL_USER,
            #     [settings.EMAIL_USER],
            #     fail_silently=False,
            #     auth_user=settings.EMAIL_USER,
            #     auth_password=settings.EMAIL_PASSWORD,
            # )
            rsvp_flag = True
    return render(
        request,
        "home.html",
        context={
            "form": form,
            "rsvp_flag": rsvp_flag,
            "contact_email": settings.CONTACT_EMAIL_USER,
        },
    )
