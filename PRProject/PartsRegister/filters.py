import django_filters
from . import models


class PartFilter(django_filters.FilterSet):
    class Meta:
        model = models.Part
        fields = {
            "identity_number": ("icontains",),
            "name": ("exact", "contains"),
            "created_date": ("lt", "gt"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters["created_date__gt"].label = "← Date (dd/mm/yyyy)"
        self.filters["created_date__lt"].label = "→ Date (dd/mm/yyyy)"


class DocFilter(django_filters.FilterSet):
    class Meta:
        model = models.Document
        fields = {
            "identity_number": ("icontains",),
            "name": ("exact",),
            "created_date": ("lt", "gt"),
            "document_type": ("exact",),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters["created_date__gt"].label = "← Date (dd/mm/yyyy)"
        self.filters["created_date__lt"].label = "→ Date (dd/mm/yyyy)"
