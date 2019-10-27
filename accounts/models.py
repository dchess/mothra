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
