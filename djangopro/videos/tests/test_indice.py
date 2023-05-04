import pytest
from django.urls import reverse
from djangopro.django_assertions import assert_contains


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('videos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp, videos):
    for video in videos:
        assert_contains(resp, video.title)


def test_link_video(resp, videos):
    for video in videos:
        video_link = reverse('videos:video', args=(video.slug,))
        assert_contains(resp, f'href="{video_link}"')
