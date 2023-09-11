import pytest
from model_bakery import baker
from djangopro.modules import facade
from djangopro.modules.models import Module


@pytest.fixture
def modules(transactional_db):
    return (baker.make(Module, title=s) for s in 'Before After'.split())


# Not working
# def test_sorted_modules(modules):
#     assert list(sorted(modules, key=lambda module: module.title)) == facade.list_modules_orderly()
