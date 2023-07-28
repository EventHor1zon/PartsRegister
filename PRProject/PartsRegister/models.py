from django.db import models
from hashid_field import HashidAutoField

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


class Part(models.Model):
    id = HashidAutoField(primary_key=True)

    identity_number = models.IntegerField(verbose_name="Identity Number" unique=True)
    description = models.TextField(max_length=500, verbose_name="Description")
    name = models.CharField(max_length=256, verbose_name="Name")
    creator = models.CharField(max_length=128, verbose_name="Creator")
    created_date = models.DateField(auto_now_add=True, verbose_name="Created On")

    manufacturer = models.CharField(max_length=256, verbose_name="Manufacturer")
    mfg_part_number = models.CharField(max_length=256, verbose_name="MFG Part Number")
    design_status = models.CharField(
        max_length=36, choices=design_statii, default="ACTIVE", verbose_name="Design Status"
    )
    sellable = models.BooleanField(verbose_name="Sellable")
    product_line = models.CharField(max_length=128, verbose_name="Product Line")

    part_type = models.ForeignKey(PartType, on_delete=models.CASCADE, verbose_name="Part Type")

    longname = models.CharField(max_length=256)
    part_number = models.CharField(max_length=16)

    def save(self, *args, **kwargs):
        self.part_number = f"{str(self.part_type.typecode).zfill(2)}-{str(self.identity_number).zfill(5)}"
        self.longname = f"{str(self.part_type.typecode).zfill(2)}-{str(self.identity_number).zfill(5)} {self.name}"

        super().save(*args, **kwargs)


## Part information classes (optional)


class PartResource(models.Model):
    name = models.CharField(max_length=256)
    url = models.URLField()

    parent = models.ForeignKey(Part, on_delete=models.CASCADE)


class ElectroMechPartInfo(models.Model):
    degild = models.BooleanField(verbose_name="De-Gild")
    pretin = models.BooleanField(verbose_name="Pre-Tin")
    reball = models.BooleanField(verbose_name="Re-Ball")
    pasted = models.BooleanField(verbose_name="Pasted")
    staked = models.BooleanField(verbose_name="Staked")
    polarity = models.CharField(max_length=256)
    material = models.CharField(max_length=256)
    power_mW = models.IntegerField(verbose_name="Power mW")
    temp = models.IntegerField(verbose_name="Temp (ppm/dC)")
    temp_min = models.IntegerField()
    temp_max = models.IntegerField()
    tolerance = models.IntegerField(verbose_name="Tolerance (+/- %)")
    value = models.IntegerField()
    footprint = models.CharField(max_length=256)
    voltage = models.IntegerField()
    quality = models.CharField(max_length=256)
    measurement_unit = models.CharField(max_length=256)
    purchase_unit = models.CharField(max_length=256)

    parent = models.ForeignKey(Part, on_delete=models.CASCADE)


class VendorPartInfo(models.Model):
    vendor = models.CharField(max_length=256)
    order_number = models.CharField(max_length=256)
    cost = models.DecimalField(decimal_places=2, max_digits=12)


class DocumentType(models.Model):
    prefix = models.CharField(max_length=6)
    name = models.CharField(max_length=128)
    shortname = models.CharField(max_length=16)


class Document(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    identity_number = models.IntegerField()
    description = models.CharField(max_length=256)
    longname = models.CharField(max_length=262)
    author = models.CharField(max_length=128)
    created_date = models.DateField(auto_now_add=True)
    document_number = models.CharField(max_length=16)

    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.document_number = (
            f"{self.document_type.prefix}-{str(self.identity_number).zfill(5)}"
        )
        self.longname = f"{self.document_type.prefix}-{str(self.identity_number).zfill(5)} {self.name}"

        super().save(*args, **kwargs)
