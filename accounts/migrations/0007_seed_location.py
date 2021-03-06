# Generated by Django 2.2.6 on 2019-11-03 21:44

import os
from django.db import migrations
from django.core.management import call_command

fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../fixtures"))
fixture_filename = "locations.json"


def load_fixture(apps, schema_editor):
    fixture_file = os.path.join(fixture_dir, fixture_filename)
    call_command("loaddata", fixture_file)


def unload_fixture(apps, schema_editor):
    "Brutally deleting all entries for this model..."

    MyModel = apps.get_model("accounts", "Location")
    MyModel.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [("accounts", "0006_seed_grade")]

    operations = [migrations.RunPython(load_fixture, reverse_code=unload_fixture)]
