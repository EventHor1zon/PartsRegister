from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django_tables2.views import SingleTableMixin, SingleTableView, MultiTableMixin
from django_filters.views import FilterView
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.forms import Form
from django.urls import reverse

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

    table_class = tables.PartsTable
    table_data = models.Part.objects.all().order_by("created_date")
    model = models.Part
    template_name = "parts.html"
    paginate_by = 50


class PartDetail(FormView):
    """did a bit of hacking to do multiple forms on a single page
    we don't actually use the built-in form_class but populate it
    because it can't be none.
    """

    template_name = "part_details.html"
    em_form = forms.NewEMInfo
    vendor_form = forms.NewVendor
    resource_form = forms.NewResource
    form_class = forms.NewEMInfo

    # would be nice to get multiple tables in to save on
    # html so try MultiTableMixin...

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["resource_form"] = self.resource_form
        context["em_form"] = self.em_form
        context["vendor_form"] = self.vendor_form
        return context

    def get(self, request, part_id):
        part = get_object_or_404(models.Part, id=part_id)
        context = self.get_context_data()
        context["part"] = part
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        """Why have a single form on a page?
        Wouldn't that be the easy and sensible thing to do?
        Yes but I have an idea and I think it's cool so now we're doing
        all this because it's not supported out the box.
        """
        print(request.POST)
        form = self.get_form_from_postdata(request)
        if form is None:
            return HttpResponse("Invalid form type", {"status_code": 500})

        if form.is_valid():
            parent = get_object_or_404(models.Part, id=request.POST["parent"])
            model = self.get_model_from_postdata(request)
            model_data = {
                k: v
                for k, v in request.POST.items()
                if k != "parent" and k != "csrfmiddlewaretoken"
            }
            # sanitise checkboxes from 'on' to True
            self.convert_boolean_form(model_data)
            model_data["parent"] = parent
            new = model(**model_data)
            try:
                new.save()
                ctx = self.get_context_data()
                ctx["part"] = parent
                ctx["status"] = "Success!"
                return self.render_to_response(ctx)
            except Exception as e:
                print(e)
                return HttpResponse(f"something derped: {e}")

    def convert_boolean_form(self, data):
        for k, v in data.items():
            if v == "on":
                data[k] = True
        return

    def get_model_from_postdata(self, request):
        if "vendor" in request.POST.keys():
            model = models.VendorPartInfo
        elif "url" in request.POST.keys():
            model = models.PartResource
        elif "temp" in request.POST.keys():
            model = models.ElectroMechPartInfo
        return model

    def get_form_from_postdata(self, request):
        if "vendor" in request.POST.keys():
            form = forms.NewVendor(request.POST)
        elif "url" in request.POST.keys():
            form = forms.NewResource(request.POST)
        elif "temp" in request.POST.keys():
            form = forms.NewEMInfo(request.POST)
        else:
            form = None
        return form


class AddPartView(FormView):
    """
    Class to handle the add part functionality. New objects are verified here
    Accepts GET and POST requests
    """

    template_name = "addpart.html"
    form_class = forms.NewPartForm

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            print(form.cleaned_data)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form: Form):
        clean = form.cleaned_data
        if "idenitity_number" not in clean.keys() or clean["identity_number"] is None:
            clean["identity_number"] = models.get_next_common_partcode(
                clean["part_type"].typecode
            )
        elif clean["identity_number"] > models.get_next_unique_partcode():
            # this will prevent users stepping forward in the database
            # they can explicitly step backwards through the global part-number
            # database so that you can create multiple parts with the same id number
            # i.e 25-10143, 18-10143, for different parts using the same product
            # however this should be done with some care. If for instance, a person
            # checks out a unique global part number (e.g 10143) and uses this code
            # to check out a part of specific type, the next part number assigned
            # will be last unique + 1. Giving users freedom means
            # giving them freedom to mess up.
            return HttpResponse("Invalid identity number!")
        else:
            obj = models.Part(**clean)
            obj.save()
            pk = obj.id
        return HttpResponseRedirect(reverse("parts", args=(pk,)))
