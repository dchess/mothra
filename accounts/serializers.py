from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Grade, Location, OrgType, Organization


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name", "is_staff")
        read_only_fields = ("email", "username", "first_name", "last_name", "is_staff")


class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grade
        fields = ("id", "level", "name")


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "name", "abbreviation")


class OrgTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrgType
        fields = ("id", "name")


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = (
            "id",
            "name",
            "size",
            "grades",
            "locations",
            "org_type",
            "grade_range",
        )
