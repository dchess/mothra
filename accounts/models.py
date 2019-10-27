from django.contrib import admin
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Grade(models.Model):
    level = models.IntegerField(
        validators=[MaxValueValidator(12), MinValueValidator(-1)]
    )
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("level",)


class Location(models.Model):
    name = models.CharField(max_length=25)
    abbreviation = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class OrgType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Organization(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField(null=True)
    grades = models.ManyToManyField(Grade)
    locations = models.ManyToManyField(Location)
    org_type = models.ForeignKey(OrgType, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class OrganizationAdmin(admin.ModelAdmin):
    list_filter = ("grades", "locations", "org_type")
