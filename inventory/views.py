from django.shortcuts import render
from rest_framework import viewsets
from .models import Domain, Subject, Product, UsageType, Usage
from .serializers import (
    DomainSerializer,
    SubjectSerializer,
    ProductSerializer,
    UsageTypeSerializer,
    UsageSerializer,
)


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UsageTypeViewSet(viewsets.ModelViewSet):
    queryset = UsageType.objects.all()
    serializer_class = UsageTypeSerializer


class UsageViewSet(viewsets.ModelViewSet):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer
