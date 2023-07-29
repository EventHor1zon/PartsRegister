import django_tables2 as tables
from django.utils.html import format_html
from . import models


class PartsTable(tables.Table):
    """
    Table to display all parts with links to part page
    TODO: Should be paginated.
    TODO: Set class and CSS
    """

    part_number = tables.TemplateColumn(
        """
            <a href="{% url 'PartsRegister:part_details' record.id %}">
                {{ record.part_number }}
            </a>
        """
    )

    part_type_str = tables.TemplateColumn(
        """
            {{ record.part_type.typename }}
        """,
        orderable=False,
    )

    class Meta:
        model = models.Part
        sequence = ("part_number", "name", "part_type_str", "created_date", "creator")
        exclude = ("id", "identity_number", "longname", "description", "part_type")
        template_name = "django_tables2/bootstrap.html"


class SinglePartTable(tables.Table):
    class Meta:
        models.Part
