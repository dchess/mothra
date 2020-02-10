from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"domains", views.DomainViewSet)
router.register(r"subjects", views.SubjectViewSet)
