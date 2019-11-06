from datetime import date
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from accounts.models import Organization


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


class Usage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    reviewer = models.ForeignKey(User, on_delete=models.PROTECT)
    can_push = models.BooleanField()
    how_push = models.TextField()
    can_pull = models.BooleanField()
    how_pull = models.TextField()
    usage_type = models.ForeignKey(UsageType, on_delete=models.PROTECT)
    is_deprecated = models.BooleanField()
    when_deprecated = models.DateField(default=date.today)
    why_deprecated = models.TextField()

    def __str__(self):
        return f"{self.organization} - {self.product}"

    class Meta:
        ordering = ("product", "organization")


class UsageAdmin(admin.ModelAdmin):
    list_filter = (
        "product",
        "organization",
        "reviewer",
        "can_push",
        "can_pull",
        "usage_type",
        "is_deprecated",
    )
