from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from .models import Profile


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

