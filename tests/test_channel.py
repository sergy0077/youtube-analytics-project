from src.channel import Channel
import pytest

def test_channel_info_fetching():
    channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'
    channel = Channel(channel_id)

    assert channel.channel_id == channel_id
    assert channel.title is not None
    assert channel.description is not None
    assert channel.url is not None
    assert channel.subscriber_count is not None
    assert channel.video_count is not None
    assert channel.view_count is not None

def test_channel_to_json(tmpdir):
    channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'
    channel = Channel(channel_id)

    filename = tmpdir.join('channel.json')
    channel.to_json(str(filename))

    assert filename.exists()

def test_channel_str():
    channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'
    channel = Channel(channel_id)

    expected_str = 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
    assert str(channel) == expected_str

def test_channel_comparison():
    channel1 = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    channel2 = Channel('UCwHL6WHUarjGfUM_586me8w')

    assert channel1.subscriber_count == 26000
    assert channel2.subscriber_count == 74400

    assert channel1 < channel2
    assert channel2 > channel1
    assert channel2 != channel1

def test_channel_arithmetic_operations():
    channel1 = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    channel2 = Channel('UCwHL6WHUarjGfUM_586me8w')

    expected_sum = channel1.subscriber_count + channel2.subscriber_count
    assert channel1 + channel2 == expected_sum

    expected_diff1 = channel1.subscriber_count - channel2.subscriber_count
    assert (channel1 - channel2) == expected_diff1

    expected_diff2 = channel2.subscriber_count - channel1.subscriber_count
    assert (channel2 - channel1) == expected_diff2



if __name__ == "__main__":
    pytest.main()