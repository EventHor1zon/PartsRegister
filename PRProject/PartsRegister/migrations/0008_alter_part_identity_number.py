# Generated by Django 4.2.3 on 2023-07-31 17:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PartsRegister", "0007_alter_electromechpartinfo_degild_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="part",
            name="identity_number",
            field=models.IntegerField(verbose_name="Identity Number"),
        ),
    ]
