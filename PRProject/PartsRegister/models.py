from django.db import models
from django.urls import reverse
from hashid_field import HashidAutoField
from datetime import date

# Create your models here.

design_statii = [
    ("ACTIVE", "Active"),
    ("INACTIVE", "Inactive"),
    ("PENDING", "Pending"),
    ("RETIRED", "Retired"),
    ("OBSOLETE", "Obsolete"),
    ("OTHER", "Other"),
]


class PartType(models.Model):
    typename = models.CharField(max_length=128)
    shortname = models.CharField(max_length=16)
    typecode = models.IntegerField()

    def __str__(self):
        return f"({self.typecode}-) {self.typename}"


class Part(models.Model):
    id = HashidAutoField(primary_key=True)

    identity_number = models.IntegerField(verbose_name="Identity Number", unique=True)
    description = models.TextField(max_length=500, verbose_name="Description")
    name = models.CharField(max_length=256, verbose_name="Name")
    creator = models.CharField(max_length=128, verbose_name="Creator")
    created_date = models.DateField(default=date.today, verbose_name="Created On")

    manufacturer = models.CharField(max_length=256, verbose_name="Manufacturer")
    mfg_part_number = models.CharField(max_length=256, verbose_name="MFG Part Number")
    design_status = models.CharField(
        max_length=36,
        choices=design_statii,
        default="ACTIVE",
        verbose_name="Design Status",
    )
    sellable = models.BooleanField(verbose_name="Sellable")
    product_line = models.CharField(max_length=128, verbose_name="Product Line")

    part_type = models.ForeignKey(
        PartType, on_delete=models.CASCADE, verbose_name="Part Type"
    )

    longname = models.CharField(max_length=256, default="")
    part_number = models.CharField(max_length=16, default="")

    def __str__(self):
        return self.longname

    def save(self, *args, **kwargs):
        self.part_number = f"{str(self.part_type.typecode).zfill(2)}-{str(self.identity_number).zfill(5)}"
        self.longname = f"{str(self.part_type.typecode).zfill(2)}-{str(self.identity_number).zfill(5)} {self.name}"

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("part_details", kwargs={"part_id": self.id})


## Part information classes (optional)


class PartResource(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=500, default="")
    url = models.URLField()

    parent = models.ForeignKey(Part, on_delete=models.CASCADE)


class ElectroMechPartInfo(models.Model):
    profile_name = models.CharField(
        max_length=256, verbose_name="Profile Name", default=""
    )
    degild = models.BooleanField(verbose_name="De-Gild", default=False)
    pretin = models.BooleanField(verbose_name="Pre-Tin", default=False)
    reball = models.BooleanField(verbose_name="Re-Ball", default=False)
    pasted = models.BooleanField(verbose_name="Pasted", default=False)
    staked = models.BooleanField(verbose_name="Staked", default=False)
    polarity = models.CharField(max_length=256)
    material = models.CharField(max_length=256)
    power_mW = models.IntegerField(verbose_name="Power mW")
    temp = models.DecimalField(
        decimal_places=3, max_digits=8, verbose_name="Temperature (ppm/dC)"
    )
    temp_min = models.DecimalField(
        decimal_places=3, max_digits=8, verbose_name="Temperature (min)"
    )
    temp_max = models.DecimalField(
        decimal_places=3, max_digits=8, verbose_name="Temperature (max)"
    )
    tolerance = models.DecimalField(
        decimal_places=3, max_digits=8, verbose_name="Tolerance (+/- %)"
    )
    value = models.IntegerField(verbose_name="Value")
    footprint = models.CharField(max_length=256, verbose_name="Footprint")
    voltage = models.DecimalField(
        decimal_places=3, max_digits=8, verbose_name="Voltage"
    )
    quality = models.CharField(max_length=256, verbose_name="Quality")
    measurement_unit = models.CharField(max_length=256, verbose_name="Measurement Unit")
    purchase_unit = models.CharField(max_length=256, verbose_name="Purchase Unit")

    parent = models.ForeignKey(Part, on_delete=models.CASCADE)


class VendorPartInfo(models.Model):
    vendor = models.CharField(max_length=256)
    order_number = models.CharField(max_length=256)
    cost = models.DecimalField(decimal_places=2, max_digits=12)

    parent = models.ForeignKey(Part, on_delete=models.CASCADE, default=None)


# Document models


class DocumentType(models.Model):
    prefix = models.CharField(max_length=6)
    name = models.CharField(max_length=128)
    shortname = models.CharField(max_length=16)


class Document(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    identity_number = models.IntegerField()
    description = models.CharField(max_length=256)
    longname = models.CharField(max_length=262, default="")
    author = models.CharField(max_length=128)
    created_date = models.DateField(auto_now_add=True)
    document_number = models.CharField(max_length=16, default="")

    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.document_number = (
            f"{self.document_type.prefix}-{str(self.identity_number).zfill(5)}"
        )
        self.longname = f"{self.document_type.prefix}-{str(self.identity_number).zfill(5)} {self.name}"

        super().save(*args, **kwargs)


def get_next_unique_partcode():
    """returns the next unique part number
    across all part types.
    """
    base = 0
    for item in Part.objects.all():
        if item.identity_number > base:
            base = item.identity_number
    return base + 1


def get_next_common_partcode(typecode: int):
    """get the next unique part number in the set of
    part types indicated by typecode
    """
    base = 0
    for item in Part.objects.filter(part_type__typecode__exact=typecode):
        if item.identity_number > base:
            base = item.identity_number
    return base + 1


def get_lowest_unique_partcode():
    """gets the first globally (all types) available
    identity number
    """
    base = 0
    qs = Part.objects.all()
    for item in qs:
        if item.identity_number == base:
            # increment base until we have
            # a free unique number
            base = base + 1
            break
    return base


def get_lowest_unique_partcode_by_type(typecode: int):
    base = 0
    qs = Part.objects.filter(part_type__typecode__exact=typecode)
    for item in qs:
        if item.identity_number == base:
            # increment base until we have
            # a free unique number
            base = base + 1
            break
    return base
