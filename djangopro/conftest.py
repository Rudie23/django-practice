import pytest
from model_bakery import baker


@pytest.fixture
def user_logged(db, django_user_model):
    user_model = baker.make(django_user_model, first_name='Dave')
    return user_model


@pytest.fixture
def client_user_logged(user_logged, client):
    client.force_login(user_logged)
    return client
