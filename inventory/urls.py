from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"domains", views.DomainViewSet)
router.register(r"subjects", views.SubjectViewSet)
router.register(r"products", views.ProductViewSet)
router.register(r"usagetypes", views.UsageTypeViewSet)
router.register(r"usages", views.UsageViewSet)
router.register(r"data_interfaces", views.DataInterfaceViewSet)


urlpatterns = [
    path("products/", views.ProductList.as_view(), name="products"),
    path("products/<int:pk>/", views.ProductDetail.as_view(), name="product"),
    path("products/<int:pk>/edit/", views.ProductUpdate.as_view(), name="edit_product"),
    path("products/create/", views.ProductCreate.as_view(), name="create_product"),
    path("reviews/create/", views.UsageCreate.as_view(), name="create_review"),
    path("reviews/<int:pk>/edit/", views.UsageUpdate.as_view(), name="edit_review"),
    path("reviews/<int:pk>/delete/", views.UsageDelete.as_view(), name="delete_review"),
]
