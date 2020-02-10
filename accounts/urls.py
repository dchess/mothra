from django.urls import path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"grades", views.GradeViewSet)
router.register(r"locations", views.LocationViewSet)
router.register(r"orgtypes", views.OrgTypeViewSet)
router.register(r"organizations", views.OrganizationViewSet)
router.register(r"profiles", views.ProfileViewSet)


urlpatterns = [
    path("members/", views.MemberList.as_view(), name="members"),
    path("orgs/", views.OrgList.as_view(), name="orgs"),
    path("", views.ProfileDetail.as_view(), name="profile"),
    path("<profile>/", views.ProfileDetail.as_view(), name="profile"),
    path("<int:pk>/edit/", views.ProfileUpdate.as_view(), name="edit_profile"),
    path("orgs/<int:pk>/edit/", views.OrgUpdate.as_view(), name="edit_org"),
    path("orgs/create/", views.OrgCreate.as_view(), name="create_org"),
    path("token/create/", views.create_token, name="create_token"),
]
