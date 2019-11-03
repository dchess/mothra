# Generated by Django 2.2.6 on 2019-11-03 21:37

import os
from django.db import migrations
from django.core.management import call_command

fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../fixtures"))
fixture_filename = "grades.json"


def load_fixture(apps, schema_editor):
    fixture_file = os.path.join(fixture_dir, fixture_filename)
    call_command("loaddata", fixture_file)


def unload_fixture(apps, schema_editor):
    "Brutally deleting all entries for this model..."

    MyModel = apps.get_model("accounts", "Grade")
    MyModel.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [("accounts", "0005_auto_20191028_0032")]

    operations = [migrations.RunPython(load_fixture, reverse_code=unload_fixture)]
