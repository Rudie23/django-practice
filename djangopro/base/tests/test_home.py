import pytest
from django.urls import reverse
from djangopro.django_assertions import assert_contains


@pytest.fixture
def response(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(response):
    assert response.status_code == 200


def test_title(response):
    assert_contains(response, '<title>Home</title>')


def test_home_link(response):
    assert_contains(response, f'href="{reverse("base:home")}">Home</a>')
