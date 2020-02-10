from django.urls import path
from . import views


urlpatterns = [
    path("members/", views.MemberList.as_view(), name="members"),
    path("orgs/", views.OrgList.as_view(), name="orgs"),
    path("", views.ProfileDetail.as_view(), name="profile"),
    path("<profile>/", views.ProfileDetail.as_view(), name="profile"),
    path("<int:pk>/edit/", views.ProfileUpdate.as_view(), name="edit_profile"),
    path("orgs/<int:pk>/edit", views.OrgUpdate.as_view(), name="edit_org"),
    path("orgs/create", views.OrgCreate.as_view(), name="create_org"),
]
