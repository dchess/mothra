import pytest
from inventory.models import Domain
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
