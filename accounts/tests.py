import pytest
from accounts.models import Grade
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

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
