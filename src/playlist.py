import json
from datetime import timedelta
from src.channel import Channel


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
        """Получение списка элементов плейлиста из API YouTube"""
        playlist_items = []
        next_page_token = None

        while True:
            response = Channel.get_service().playlistItems().list(
                part='contentDetails',
                playlistId=self.playlist_id,
                maxResults=50,
                pageToken=next_page_token
            ).execute()

            # Вывод полученного ответа от YouTube API
            print(json.dumps(response, indent=2))

            playlist_items.extend(response['items'])

            for video in response['items']:
                print(video)  # Добавить эту строку для печати содержимого каждого элемента видео

                contentDetails = video['contentDetails']
                playlist_items.append(contentDetails)

            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
        return playlist_items

    @property
    def total_duration(self):
        """Вычисление общей продолжительности плейлиста"""
        total_duration = timedelta()
        self.playlist_items = self._fetch_playlist_items()  # сохранить список элементов плейлиста
        for video in self.playlist_items:
            if 'contentDetails' in video and 'duration' in video['contentDetails']:
                duration_str = video['contentDetails']['duration']
                duration = self._parse_duration(duration_str)

                print(f"Video ID: {video['contentDetails']['videoId']}")
                print(f"Duration: {duration_str}")
                print(f"Parsed Duration: {duration}")

                total_duration += duration
        return total_duration

    def total_seconds(self):
        """Вычисление общего количества секунд в продолжительности плейлиста"""
        return self.total_duration.total_seconds()

    @staticmethod
    def _parse_duration(duration_str):
        """Парсинг строки продолжительности и преобразование в timedelta"""
        duration_parts = duration_str.replace('PT', '').lower().split('h')
        hours = int(duration_parts[0]) if duration_parts[0] else 0
        minutes, seconds = map(int, duration_parts[-1].strip('ms').split('m'))

        print(f"Hours: {hours}")
        print(f"Minutes: {minutes}")
        print(f"Seconds: {seconds}")

        duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        print(duration)
        return duration

    def show_best_video(self):
        """Вывод наилучшего видео из плейлиста"""
        sorted_videos = sorted(self.playlist_items, key=lambda video: int(video.get('statistics', {}).get('likeCount',
                                                                                                          {}).get(
            'value', 0)), reverse=True)

        best_video_id = sorted_videos[0]['contentDetails']['videoId']
        return f"https://youtu.be/{best_video_id}"
