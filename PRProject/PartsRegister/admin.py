from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Part)
admin.site.register(models.PartType)
admin.site.register(models.PartResource)
admin.site.register(models.VendorPartInfo)
