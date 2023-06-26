from typing import List

import pytest
from django.urls import reverse
from djangopro.django_assertions import assert_contains
from model_bakery import baker

from djangopro.modules.models import Module, Lesson


@pytest.fixture
def modules(db):
    return baker.make(Module, 2)


@pytest.fixture
def lessons(modules):
    lessons = list()
    for module in modules:
        lessons.extend(baker.make(Lesson, 3, module=module))
    return lessons


@pytest.fixture
def resp(client, modules, lessons):
    resp = client.get(reverse('modules:index'))
    return resp


def test_available_index(resp):
    assert resp.status_code == 200


def test_module_title(resp, modules: List[Module]):
    for module in modules:
        assert_contains(resp, module.title)


def test_description(resp, modules: List[Module]):
    for module in modules:
        assert_contains(resp, module.description)


def test_public(resp, modules: List[Module]):
    for module in modules:
        assert_contains(resp, module.public)


def test_lesson_titles(resp, lessons: List[Lesson]):
    for lesson in lessons:
        assert_contains(resp, lesson.title)


def test_lessons_url(resp, lessons: List[Lesson]):
    for lesson in lessons:
        assert_contains(resp, lesson.get_absolute_url())
#
#
# def test_lesson_links(resp, lessons):
#     for lesson in lessons:
#         assert_contains(resp, lesson.get_absolute_url())
