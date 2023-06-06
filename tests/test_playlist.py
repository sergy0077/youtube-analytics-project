from datetime import timedelta
import pytest
from src.playlist import PlayList


@pytest.fixture
def playlist():
    return PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')


def test_playlist_id_initialization(playlist):
    assert playlist.playlist_id == 'PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw'


def test_playlist_info(playlist):
    assert playlist.title == "Moscow Python Meetup №81"
    assert playlist.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"


def test_total_duration(playlist):
    assert str(playlist.total_duration) == "1:49:52"
    assert isinstance(playlist.total_duration, timedelta)
    assert playlist.total_duration.total_seconds() == 6592.0


def test_show_best_video(playlist, monkeypatch):
    mock_playlist_items = {
        'items': [
            {
                'id': 'cUGyMzWQcGM',
                'statistics': {'likeCount': 10}
            },
            {
                'id': 'video2',
                'statistics': {'likeCount': 5}
            },
            {
                'id': 'video3',
                'statistics': {'likeCount': 8}
            }
        ]
    }

    monkeypatch.setattr(playlist, 'playlist_items', mock_playlist_items)

    assert playlist.show_best_video() == "https://youtu.be/cUGyMzWQcGM"


if __name__ == "__main__":
    pytest.main()
