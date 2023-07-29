from django.urls import path, re_path
from . import views

app_name = "PartsRegister"
urlpatterns = [
    path("", views.index, name="index"),
    path("parts/", views.PartsView.as_view(), name="parts"),
    re_path(
        r"^part_details/(?P<part_id>[0-z]+)$", views.part_view, name="part_details"
    ),
    path("addpart/", views.AddPartView.as_view(), name="addpart"),
]
