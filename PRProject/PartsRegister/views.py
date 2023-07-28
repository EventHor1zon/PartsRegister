from django.shortcuts import render, get_object_or_404
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from django.http import HttpResponse
from django.views import View
from . import models
from . import tables

# Create your views here.


def index(request):
    return HttpResponse("Welcome to the Parts & Document Number Registry")


def part_view(request, part_id):
    part = get_object_or_404(models.Part, id=part_id)
    return render(request, "part_details.html", {"part": part})


class PartsView(SingleTableMixin, FilterView):
    # def get(self, request):
    #     table = tables.PartsTable(models.Part.objects.all())
    #     table.paginate(page=request.GET.get("page", 1), per_page=100)
    #     return render(request, "parts.html", {"table": table})
    table_class = tables.PartsTable
    table_data = models.Part.objects.all().order_by("created_date")
    model = models.Part
    template_name = "parts.html"
    paginate_by = 50
