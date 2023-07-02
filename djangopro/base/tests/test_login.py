import pytest
from django.urls import reverse
from model_bakery import baker

from djangopro.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


def test_login_form_page(resp):
    assert resp.status_code == 200


@pytest.fixture
def user(db, django_user_model):
    user_model = baker.make(django_user_model)
    password = 'password'
    user_model.set_password(password)
    user_model.save()
    user_model.password_full = password
    return user_model


@pytest.fixture
def resp_post(client, user):
    return client.post(reverse('login'), {'username': user.email, 'password': user.password_full})


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302


def test_login_redirect_page(resp_post):
    assert resp_post.url == reverse('modules:index')


@pytest.fixture
def resp_home(client, db):
    return client.get(reverse('base:home'))


def test_button_available(resp_home):
    assert_contains(resp_home, 'Sign in')


@pytest.fixture
def resp_home_user_logged(client_user_logged, db):
    return client_user_logged.get(reverse('base:home'))


def test_button_unavailable(resp_home_user_logged):
    assert_not_contains(resp_home_user_logged, 'Sign in')


def test_link_login_unavailable(resp_home_user_logged):
    assert_not_contains(resp_home_user_logged, reverse('login'))


def test_button_logout_available(resp_home_user_logged):
    assert_contains(resp_home_user_logged, 'Log out')


def test_user_name_available(resp_home_user_logged, user_logged):
    assert_contains(resp_home_user_logged, user_logged.first_name)


def test_link_logout_available(resp_home_user_logged):
    assert_contains(resp_home_user_logged, reverse('logout'))
