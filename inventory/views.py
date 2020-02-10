from django.shortcuts import render
from rest_framework import viewsets
from .models import Domain, Subject
from .serializers import DomainSerializer, SubjectSerializer


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
