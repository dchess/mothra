from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from rest_framework import viewsets
from .models import Domain, Subject, Product, UsageType, Usage
from .serializers import (
    DomainSerializer,
    SubjectSerializer,
    ProductSerializer,
    UsageTypeSerializer,
    UsageSerializer,
)


class ProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products.html"


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = "__all__"
    template_name = "product_update_form.html"


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = "__all__"
    template_name = "product_create_form.html"


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
