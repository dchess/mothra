from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Grade


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name", "is_staff")
        read_only_fields = ("email", "username", "first_name", "last_name", "is_staff")


class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grade
        fields = ("id", "level", "name")
