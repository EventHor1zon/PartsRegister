from django import forms
from django.forms import ModelForm
from . import models


class NewPartForm(forms.ModelForm):
    identity_number = forms.IntegerField(max_value=99999, required=False)

    class Meta:
        model = models.Part
        fields = [
            "name",
            "description",
            "creator",
            "manufacturer",
            "mfg_part_number",
            "design_status",
            "product_line",
            "part_type",
            "sellable",
        ]


class NewResource(forms.ModelForm):
    class Meta:
        model = models.PartResource
        exclude = ["parent"]


class NewEMInfo(forms.ModelForm):
    class Meta:
        model = models.ElectroMechPartInfo
        exclude = ["parent"]


class NewVendor(forms.ModelForm):
    class Meta:
        model = models.VendorPartInfo
        exclude = ["parent"]


#     name = forms.CharField(max_length=256)
#     description = forms.CharField(max_length=500)
#     creator = forms.CharField(max_length=128)
#     manufacturer = forms.CharField(max_length=256)
#     mfg_part_number = forms.CharField(max_length=256)
#     design_status = forms.ChoiceField()
