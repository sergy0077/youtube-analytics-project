from datetime import timedelta
from src.channel import Channel
from isodate import parse_duration


def _get_seconds_multiplier(time_format):
    """Получение множителя для формата времени"""
    if time_format == 'P' or time_format == 'PT':
        return 1
    if time_format == 'H':
        return 3600
    if time_format == 'M':
        return 60
    if time_format == 'S':
        return 1


class PlayList:
    """Класс, представляющий плейлист YouTube"""

    def __init__(self, playlist_id):
        """Инициализация плейлиста с заданным идентификатором"""
        self.playlist_id = playlist_id
        self.title = None
        self.url = None
        self.playlist_items = []

        self._fetch_playlist_info()
        self._fetch_playlist_items()

    def _fetch_playlist_info(self):
        """Получение информации о плейлисте из API YouTube"""
        response = Channel.get_service().playlists().list(
            part='snippet',
            id=self.playlist_id
        ).execute()

        if 'items' in response:
            playlist_info = response['items'][0]['snippet']
            self.title = playlist_info['title']
            self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"

    def _fetch_playlist_items(self):

        response = Channel.get_service().playlistItems().list(
            part='contentDetails',
            playlistId=self.playlist_id,
            maxResults=50
        ).execute()

        playlist_items = [item['contentDetails']['videoId'] for item in response['items']]

        playlist_items_response = Channel.get_service().videos().list(
            part='contentDetails, statistics',
            id=','.join(playlist_items)
        ).execute()

        return playlist_items_response

    @property
    def total_duration(self):
        """Вычисление общей продолжительности плейлиста"""
        total_duration = timedelta()
        self.playlist_items = self._fetch_playlist_items()  # сохранить список элементов плейлиста

        for video in self.playlist_items['items']:

            if 'contentDetails' in video and 'duration' in video['contentDetails']:
                duration_str = video['contentDetails']['duration']
                iso_duration = parse_duration(duration_str)

                print(f"Video ID: {video['id']}")
                print(f"Duration: {duration_str}")
                print(f"Parsed Duration: {iso_duration}")

                total_duration += iso_duration

        return total_duration

    def show_best_video(self):
        """Вывод наилучшего видео из плейлиста"""
        sorted_videos = sorted(self.playlist_items['items'], key=lambda video: video.get('statistics').get('likeCount'),
                               reverse=True)

        best_video_id = sorted_videos[0]['id']
        return f"https://youtu.be/{best_video_id}"
