from django.urls import path

from . import views

app_name = "PartsRegister"
urlpatterns = [
    path("", views.index, name="index"),
    path(r"^parts/(?P<part_id>[0-z]+)$", views.part_view, name="part"),
]
