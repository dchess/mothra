from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from rest_framework import viewsets
from .models import Organization, Profile, Grade
from .serializers import UserSerializer, GradeSerializer


@method_decorator(login_required, name="dispatch")
class ProfileDetail(DetailView):
    template_name = "profile.html"

    def get_object(self):
        try:
            return get_object_or_404(Profile, user__username=self.kwargs["profile"])
        except KeyError:
            obj, created = Profile.objects.get_or_create(user=self.request.user)
            return obj or created


@method_decorator(login_required, name="dispatch")
class MemberList(ListView):
    queryset = Profile.objects.filter(user__is_superuser=False)
    template_name = "members.html"


@method_decorator(login_required, name="dispatch")
class ProfileUpdate(UpdateView):
    model = Profile
    fields = ["github_id", "organization"]
    template_name = "profile_update_form.html"


@method_decorator(login_required, name="dispatch")
class OrgList(ListView):
    model = Organization
    template_name = "orgs.html"


@method_decorator(login_required, name="dispatch")
class OrgUpdate(UpdateView):
    model = Organization
    fields = "__all__"
    template_name = "org_update_form.html"


@method_decorator(login_required, name="dispatch")
class OrgCreate(CreateView):
    model = Organization
    fields = "__all__"
    template_name = "org_create_form.html"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all().order_by("level")
    serializer_class = GradeSerializer
