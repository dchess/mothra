import pytest
from inventory.models import Domain, Subject
from django.core.exceptions import ValidationError

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
