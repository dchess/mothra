from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from .models import (
    Organization,
    Profile,
    Grade,
    Location,
    OrgType,
    UserProfileForm,
    ProfileForm,
)
from inventory.models import Usage
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
        if context["profile"].user == self.request.user:
            try:
                context["token"] = Token.objects.get(user=self.request.user)
            except Token.DoesNotExist:
                context["token"] = None
        search = self.request.GET.get("search")
        if search:
            context["products"] = (
                context["profile"]
                .products.annotate(
                    search=SearchVector("name", "domain__name", "subject__name")
                )
                .filter(search__icontains=search)
            )
        else:
            context["products"] = context["profile"].products.all()
        return context

    def get_object(self):
        try:
            return get_object_or_404(Profile, user__username=self.kwargs["profile"])
        except KeyError:
            obj, created = Profile.objects.get_or_create(user=self.request.user)
            return obj or created


class MemberList(LoginRequiredMixin, ListView):
    template_name = "members.html"

    def get_queryset(self):
        try:
            search = self.request.GET["search"]
            users = (
                User.objects.annotate(
                    search=SearchVector(
                        "first_name",
                        "last_name",
                        "email",
                        "profile__organization__name",
                    )
                )
                .filter(search__icontains=search)
                .order_by("first_name", "last_name")
            )
            return users
        except KeyError:
            return User.objects.all().order_by("first_name", "last_name")


@login_required
def edit_profile(request):
    if request.method == "POST":
        print(request.POST)
        user_form = UserProfileForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST)

        if all([user_form.is_valid(), profile_form.is_valid()]):
            user = user_form.save()
            profile = profile_form.save()
            return redirect("profile")
    else:
        user_form = UserProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(
        request,
        "profile_update_form.html",
        {"user_form": user_form, "profile_form": profile_form},
    )


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
