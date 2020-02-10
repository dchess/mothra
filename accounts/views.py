from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from .models import Organization, Profile, Grade, Location, OrgType
from .serializers import (
    UserSerializer,
    GradeSerializer,
    LocationSerializer,
    OrgTypeSerializer,
    OrganizationSerializer,
    ProfileSerializer,
)


class ProfileDetail(LoginRequiredMixin, DetailView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["token"] = Token.objects.get(user=self.request.user)
        except Token.DoesNotExist:
            context["token"] = None
        return context

    def get_object(self):
        try:
            return get_object_or_404(Profile, user__username=self.kwargs["profile"])
        except KeyError:
            obj, created = Profile.objects.get_or_create(user=self.request.user)
            return obj or created


class MemberList(LoginRequiredMixin, ListView):
    queryset = Profile.objects.filter(user__is_superuser=False)
    template_name = "members.html"


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ["github_id", "organization"]
    template_name = "profile_update_form.html"


class OrgList(LoginRequiredMixin, ListView):
    model = Organization
    template_name = "orgs.html"


class OrgUpdate(LoginRequiredMixin, UpdateView):
    model = Organization
    fields = "__all__"
    template_name = "org_update_form.html"


class OrgCreate(LoginRequiredMixin, CreateView):
    model = Organization
    fields = "__all__"
    template_name = "org_create_form.html"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class OrgTypeViewSet(viewsets.ModelViewSet):
    queryset = OrgType.objects.all()
    serializer_class = OrgTypeSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


@login_required
def create_token(request):
    try:
        Token.objects.create(user=request.user)
        return redirect("profile")
    except IntegrityError:
        return redirect("profile")
