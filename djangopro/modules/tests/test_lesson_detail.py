import pytest
from django.urls import reverse
from djangopro.django_assertions import assert_contains
from model_bakery import baker

from djangopro.modules.models import Module, Lesson


@pytest.fixture
def module(db):
    return baker.make(Module)


@pytest.fixture
def lesson(module):
    return baker.make(Lesson, module=module)


@pytest.fixture
def resp(client_user_logged, lesson):
    resp = client_user_logged.get(reverse('modules:lesson', kwargs={'slug': lesson.slug}))
    return resp


def test_lesson_title(resp, lesson: Lesson):
    assert_contains(resp, lesson.title)


def test_vimeo(resp, lesson: Lesson):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{lesson.vimeo_id}')


def test_module_breadcrumb(resp, module: Module):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{module.get_absolute_url()}">{module.title}</a></li>')


@pytest.fixture
def resp_not_logged(client, lesson):
    resp = client.get(reverse('modules:lesson', kwargs={'slug': lesson.slug}))
    return resp


def test_not_logged_redirect(resp_not_logged):
    assert resp_not_logged.status_code == 302
    assert resp_not_logged.url.startswith(reverse('login'))
