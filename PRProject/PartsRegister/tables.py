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
        model = models.Part
        exclude = {
            "identity_number",
            "description",
            "part_type",
            "longname",
            "part_number",
        }

    def render_design_status(self, value):
        if value == "ACTIVE":
            return f'<bold style="background-color: greenyellow;">{value}</b>'
        elif value == "PENDING":
            return f'<bold style="background-color: orange;">{value}</bold>'
        else:
            return f'<bold style="background-color: red;">{value}</bold>'


class EmInfoTable(tables.Table):
    class Meta:
        model = models.ElectroMechPartInfo
        exclude = {"parent"}


class VendorInfoTable(tables.Table):
    class Meta:
        model = models.VendorPartInfo
        exclude = {"parent"}


class ResourceInfoTable(tables.Table):
    class Meta:
        model = models.PartResource
        exclude = {"parent"}
