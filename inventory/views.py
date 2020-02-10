from django.shortcuts import render
from rest_framework import viewsets
from .models import Domain
from .serializers import DomainSerializer


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
