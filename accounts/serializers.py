from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Grade, Location, OrgType


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
