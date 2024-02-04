from django.contrib import admin
from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path(r"^$", views.home, name="home"),
    re_path(r"^admin/", admin.site.urls),
    re_path("^accounts/", include("django.contrib.auth.urls")),
    re_path("^rsvp/", views.rsvp, name="rsvp"),
]
