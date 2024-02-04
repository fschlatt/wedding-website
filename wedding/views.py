from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import GuestsForm


def home(request):
    if request.method == "POST":
        # TODO find out how to connect form to fields in html
        form = GuestsForm(request.POST)
        print(form)
        if form.is_valid():
            return HttpResponseRedirect("/rsvp/")
    else:
        form = GuestsForm()
    return render(
        request,
        "home.html",
        context={
            "support_email": settings.DEFAULT_WEDDING_REPLY_EMAIL,
            "website_url": settings.WEDDING_WEBSITE_URL,
            "couple_name": settings.BRIDE_AND_GROOM,
            "wedding_location": settings.WEDDING_LOCATION,
            "wedding_date": settings.WEDDING_DATE,
            "form": form,
        },
    )


def rsvp(request):
    return render(request, "base.html")
