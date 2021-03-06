# Generated by Django 3.0.3 on 2020-02-22 19:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_subject_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='usage',
            name='rating',
            field=models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usage',
            name='review',
            field=models.TextField(blank=True),
        ),
    ]
