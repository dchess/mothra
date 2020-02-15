from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


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
    size = models.IntegerField(null=True, blank=True)
    grades = models.ManyToManyField(Grade)
    locations = models.ManyToManyField(Location)
    org_type = models.ForeignKey(OrgType, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("orgs")

    @property
    def grade_range(self):
        min_grade = self.grades.all().order_by("level")[0]
        max_grade = self.grades.all().order_by("-level")[0]
        return f"{min_grade}-{max_grade}"

    class Meta:
        ordering = ("name",)


class OrganizationAdmin(admin.ModelAdmin):
    list_filter = ("grades", "locations", "org_type")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    github_id = models.CharField(max_length=39, null=True, blank=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.PROTECT, null=True, blank=True
    )
    products = models.ManyToManyField("inventory.Product", through="inventory.Usage")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile", kwargs={"profile": self.user})

    class Meta:
        ordering = ("user",)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "organization")
    list_filter = ("organization",)
    search_fields = ["user", "organization"]
