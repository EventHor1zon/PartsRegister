import django_filters
from . import models


class PartFilter(django_filters.FilterSet):
    class Meta:
        model = models.Part
        fields = {
            "identity_number": ("icontains", "iexact"),
            "name": ("contains", "exact"),
            "created_date": ("lt", "gt"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters["created_date__gt"].label = "← Date (dd/mm/yyyy)"
        self.filters["created_date__lt"].label = "→ Date (dd/mm/yyyy)"
