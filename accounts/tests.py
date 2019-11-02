import pytest
from accounts.models import Grade, Location, OrgType, Organization, Profile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db.models.deletion import ProtectedError

pytestmark = pytest.mark.django_db


@pytest.fixture
def grade():
    return Grade.objects.create(level=0, name="K")


def test_grade_string_representation(grade):
    assert str(grade) == grade.name


def test_grade_min_level(grade):
    with pytest.raises(ValidationError):
        grade.level = -5
        grade.full_clean()


def test_grade_max_level(grade):
    with pytest.raises(ValidationError):
        grade.level = 13
        grade.full_clean()


def test_grade_correct_level(grade):
    for level in range(1, 13):
        grade.level = level
        grade.full_clean()


def test_grade_name_max_length(grade):
    with pytest.raises(ValidationError):
        grade.name = "K" * 3
        grade.full_clean()


def test_grade_name_correct_length(grade):
    grade.name = "TK"
    grade.full_clean()


def test_grade_level_is_required():
    with pytest.raises(IntegrityError):
        grade = Grade.objects.create(name="E")
        grade.full_clean()


def test_grade_name_is_required():
    with pytest.raises(ValidationError):
        grade = Grade.objects.create(level=0)
        grade.full_clean()


@pytest.fixture
def location():
    return Location.objects.create(abbreviation="CA", name="California")


def test_location_string_representation(location):
    assert str(location) == location.name


def test_location_name_max_length(location):
    with pytest.raises(ValidationError):
        location.name = "x" * 26
        location.full_clean()


def test_location_abbreviation_max_length(location):
    with pytest.raises(ValidationError):
        location.abbreviation = "x" * 3
        location.full_clean()


def test_location_name_is_required():
    with pytest.raises(ValidationError):
        location = Location.objects.create(abbreviation="CA")
        location.full_clean()


def test_location_abbreviation_is_required():
    with pytest.raises(ValidationError):
        location = Location.objects.create(name="California")
        location.full_clean()


@pytest.fixture
def org_type():
    return OrgType.objects.create(name="charter management organization")


def test_org_type_string_representation(org_type):
    assert str(org_type) == org_type.name


def test_org_type_max_length(org_type):
    with pytest.raises(ValidationError):
        org_type.name = "x" * 51
        org_type.full_clean()


def test_org_type_name_is_required():
    with pytest.raises(ValidationError):
        org_type = OrgType.objects.create(name="")
        org_type.full_clean()


@pytest.fixture
def organization(location, org_type):
    # create test grades for HS (9-12)
    for grade in range(9, 13):
        Grade.objects.create(level=grade, name=f"{grade}")

    grades = Grade.objects.filter(level__gte=9)
    organization = Organization.objects.create(
        name="Test Organization", size=12, org_type=org_type
    )

    organization.grades.set(grades)
    organization.save()
    return organization


def test_organization_string_representation(organization):
    assert str(organization) == organization.name


def test_organization_name_max_length(organization):
    with pytest.raises(ValidationError):
        organization.name = "x" * 51
        organization.full_clean()


def test_organization_size_can_be_null(organization):
    organization.size = None
    organization.full_clean()


def test_organization_name_is_required(org_type):
    with pytest.raises(ValidationError):
        organization = Organization.objects.create(size=10, org_type=org_type)
        organization.full_clean()


def test_org_type_protected_delete(organization, org_type):
    with pytest.raises(ProtectedError):
        org_type.delete()


def test_org_type_is_required():
    with pytest.raises(IntegrityError):
        organization = Organization.objects.create(size=10, name="Test Org 2")
        organization.full_clean()


def test_organization_size_is_not_required(org_type):
    organization = Organization.objects.create(name="Test Org 3", org_type=org_type)
    organization.full_clean()


@pytest.fixture
def user():
    return User.objects.create_user("test_user", password="Testpassword")


@pytest.fixture
def profile(user, organization):
    return Profile.objects.create(
        user=user, github_id="test_user", organization=organization
    )


def test_profile_string_representation(profile):
    assert str(profile) == profile.user.username


def test_profile_github_id_max_length(profile):
    with pytest.raises(ValidationError):
        profile.github_id = "x" * 40
        profile.full_clean()


def test_profile_organization_is_required(profile):
    with pytest.raises(ValidationError):
        profile.organization = None
        profile.full_clean()

def test_profile_user_is_required(profile):
    with pytest.raises(ValidationError):
        profile.user = None
        profile.full_clean()
