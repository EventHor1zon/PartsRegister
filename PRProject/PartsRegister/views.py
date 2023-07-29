from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from django.http import HttpResponse
from django.views import View

from . import models
from . import tables
from . import forms

# Create your views here.


def index(request):
    """
    The index page.
    """
    part_num = len(models.Part.objects.all())
    doc_num = len(models.Document.objects.all())
    return render(
        request, "index.html", context={"partnum": part_num, "docnum": doc_num}
    )


def part_view(request, part_id):
    part = get_object_or_404(models.Part, id=part_id)
    return render(request, "part_details.html", {"part": part})


class PartsView(SingleTableMixin, FilterView):
    """
    class to handle the main table of the parts register
    Only accepts GET requests
    """

    # def get(self, request):
    #     table = tables.PartsTable(models.Part.objects.all())
    #     table.paginate(page=request.GET.get("page", 1), per_page=100)
    #     return render(request, "parts.html", {"table": table})
    table_class = tables.PartsTable
    table_data = models.Part.objects.all().order_by("created_date")
    model = models.Part
    template_name = "parts.html"
    paginate_by = 50


class AddPartView(FormView):
    """
    Class to handle the add part functionality. New objects are verified here
    Accepts GET and POST requests
    """

    template_name = "addpart.html"
    form_class = forms.NewPartForm
