import pytest
from datetime import timedelta
from src.playlist import PlayList


@pytest.fixture
def playlist():
    return PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')


def test_playlist_info(playlist):
    assert playlist.title == "Moscow Python Meetup №81"
    assert playlist.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"


def test_total_duration(playlist):
    assert str(playlist.total_duration) == "1:49:52"
    assert isinstance(playlist.total_duration, timedelta)
    assert playlist.total_duration.total_seconds() == 6592.0


def test_show_best_video(playlist):
    assert playlist.show_best_video() == "https://youtu.be/cUGyMzWQcGM"


if __name__ == "__main__":
    pytest.main()
