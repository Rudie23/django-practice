import pytest
from django.urls import reverse
from djangopro.django_assertions import assert_contains
from model_bakery import baker

from djangopro.modules.models import Module


@pytest.fixture
def modules(db):
    return baker.make(Module, 2)


@pytest.fixture
def resp(client, modules):
    resp = client.get(reverse('base:home'))
    return resp


def test_module_title(resp, modules):
    for module in modules:
        assert_contains(resp, module.title)


def test_link_modules(resp, modules):
    for modulo in modules:
        assert_contains(resp, modulo.get_absolute_url())
