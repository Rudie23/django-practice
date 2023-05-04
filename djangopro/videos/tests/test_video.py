import pytest
from django.urls import reverse
from djangopro.django_assertions import assert_contains


# Create your tests here.

@pytest.fixture
def resp(client, video):
    return client.get(reverse('videos:video', args=(video.slug,)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp, video):
    assert_contains(resp, video.title)


def test_content_video(resp, video):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}"')

