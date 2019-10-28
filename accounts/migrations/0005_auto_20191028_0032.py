# Generated by Django 2.2.6 on 2019-10-28 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_id', models.CharField(max_length=39)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Organization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
    ]
