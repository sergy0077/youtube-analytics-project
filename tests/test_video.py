from src.video import Video, PLVideo
import pytest


def test_video_attributes():
    video = Video('AWX4JnAnjBE')
    assert video.id == 'AWX4JnAnjBE'
    assert video.title == 'GIL в Python: зачем он нужен и как с этим жить'
    assert video.link == 'https://youtube.com/watch?v=AWX4JnAnjBE'
    assert video.views == 1000
    assert video.likes == 500


def test_video_string_representation():
    video = Video('AWX4JnAnjBE')
    assert str(video) == 'GIL в Python: зачем он нужен и как с этим жить'


def test_plvideo_attributes():
    plvideo = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert plvideo.id == '4fObz_qw9u4'
    assert plvideo.title == 'MoscowPython Meetup 78 - вступление'
    assert plvideo.link == 'https://youtube.com/watch?v=4fObz_qw9u4'
    assert plvideo.views == 1000
    assert plvideo.likes == 500
    assert plvideo.playlist_id == 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC'


def test_plvideo_string_representation():
    plvideo = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert str(plvideo) == 'MoscowPython Meetup 78 - вступление'


if __name__ == "__main__":
    pytest.main()
