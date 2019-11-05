from django.db import models
from django.contrib import admin


class Domain(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Subject(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Product(models.Model):
    name = models.CharField(max_length=100)
    domain = models.ForeignKey(Domain, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class ProductAdmin(admin.ModelAdmin):
    list_filter = ("domain", "subject")
    list_display = ("name", "domain", "subject")
    search_fields = ["name"]


class UsageType(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
