from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from rest_framework import viewsets
from .models import Domain, Subject, Product, UsageType, Usage, DataInterface
from .serializers import (
    DomainSerializer,
    SubjectSerializer,
    ProductSerializer,
    UsageTypeSerializer,
    UsageSerializer,
    DataInterfaceSerializer,
)


class ProductList(LoginRequiredMixin, ListView):
    template_name = "products.html"

    def get_queryset(self):
        try:
            search = self.request.GET["search"]
            products = Product.objects.annotate(
                search=SearchVector("name", "domain__name", "subject__name")
            ).filter(search__icontains=search)
            return products
        except KeyError:
            return Product.objects.all()


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = "__all__"
    template_name = "product_update_form.html"


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = "__all__"
    template_name = "product_create_form.html"


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Usage.objects.filter(product=self.get_object())
        total_reviews = float(reviews.count())
        if total_reviews > 0:
            promoters = (reviews.filter(rating=5).count() / total_reviews) * 100
            detractors = (reviews.filter(rating__lte=3).count() / total_reviews) * 100
            context["NPS"] = int(promoters - detractors)
        return context


class UsageCreate(LoginRequiredMixin, CreateView):
    model = Usage
    fields = "__all__"
    template_name = "usage_create_form.html"

    def get_success_url(self):
        return reverse("profile")


class UsageUpdate(LoginRequiredMixin, UpdateView):
    model = Usage
    fields = "__all__"
    template_name = "usage_update_form.html"

    def get_success_url(self):
        return reverse("profile")


class UsageDelete(LoginRequiredMixin, DeleteView):
    model = Usage
    template_name = "usage_confirm_delete.html"
    success_url = reverse_lazy("profile")


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


class DataInterfaceViewSet(viewsets.ModelViewSet):
    queryset = DataInterface.objects.all()
    serializer_class = DataInterfaceSerializer
