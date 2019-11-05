import pytest
from inventory.models import Domain, Subject, Product
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db.models.deletion import ProtectedError

pytestmark = pytest.mark.django_db


@pytest.fixture
def domain():
    return Domain.objects.create(name="Test Domain")


def test_domain_string_representation(domain):
    assert str(domain) == domain.name


def test_domain_name_max_length(domain):
    with pytest.raises(ValidationError):
        domain.name = "x" * 51
        domain.full_clean()


@pytest.fixture
def subject():
    return Subject.objects.create(name="Test Subject")


def test_subject_string_representation(subject):
    assert str(subject) == subject.name


def test_subject_name_max_length(subject):
    with pytest.raises(ValidationError):
        subject.name = "x" * 26
        subject.full_clean()


@pytest.fixture
def product(domain, subject):
    return Product.objects.create(name="Test Product", domain=domain, subject=subject)


def test_product_string_representation(product):
    assert str(product) == product.name


def test_product_name_max_length(product):
    with pytest.raises(ValidationError):
        product.name = "x" * 101
        product.full_clean()


def test_product_requires_domain(product, subject):
    with pytest.raises(IntegrityError):
        product = Product.objects.create(name="Test Product 2", subject=subject)
        product.full_clean()


def test_product_requires_subject(product, domain):
    with pytest.raises(IntegrityError):
        product = Product.objects.create(name="Test Product 3", domain=domain)
        product.full_clean()


def test_product_protects_deleting_domain(product, domain):
    with pytest.raises(ProtectedError):
        domain.delete()


def test_product_protects_deleting_subject(product, subject):
    with pytest.raises(ProtectedError):
        subject.delete()
