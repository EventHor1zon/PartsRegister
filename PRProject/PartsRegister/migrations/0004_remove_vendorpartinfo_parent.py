# Generated by Django 4.2.3 on 2023-07-28 04:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "PartsRegister",
            "0003_vendorpartinfo_parent_alter_document_document_number_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vendorpartinfo",
            name="parent",
        ),
    ]