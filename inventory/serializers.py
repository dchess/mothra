from rest_framework import serializers
from .models import Domain, Subject, Product, UsageType


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class UsageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageType
        fields = "__all__"
