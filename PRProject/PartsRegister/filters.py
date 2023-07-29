import django_filters
from . import models


class PartFilter(django_filters.FilterSet):
    class Meta:
        model = models.Part
        fields = []
