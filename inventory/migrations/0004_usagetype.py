# Generated by Django 2.2.6 on 2019-11-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
