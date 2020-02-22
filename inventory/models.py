from datetime import date
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from accounts.models import Organization, Profile


class Domain(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default="#000000")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Subject(models.Model):
    name = models.CharField(max_length=25)
    icon = models.CharField(max_length=50, default="fas fa-brain")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Product(models.Model):
    name = models.CharField(max_length=100)
    domain = models.ForeignKey(Domain, on_delete=models.PROTECT)
    subject = models.ForeignKey(
        Subject, on_delete=models.PROTECT, null=True, blank=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products")

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


class DataInterface(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Usage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    reviewer = models.ForeignKey(Profile, on_delete=models.PROTECT)
    how_push = models.ForeignKey(
        DataInterface,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="push_type",
    )
    how_pull = models.ForeignKey(
        DataInterface,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="pull_type",
    )
    usage_type = models.ForeignKey(UsageType, on_delete=models.PROTECT)
    is_deprecated = models.BooleanField()
    when_deprecated = models.DateField(blank=True, null=True)
    why_deprecated = models.TextField(blank=True, null=True)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    review = models.TextField(blank=True)

    def __str__(self):
        return f"{self.organization} - {self.product}"

    class Meta:
        ordering = ("product", "organization")


class UsageAdmin(admin.ModelAdmin):
    list_filter = ("product", "organization", "reviewer", "usage_type", "is_deprecated")
