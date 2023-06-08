from googleapiclient.discovery import build
import os


class Video:
    def __init__(self, video_id):
        try:
            # Получение данных о видео из API
            video_data = self._get_video_data(video_id)

            # Инициализация атрибутов экземпляра класса Video
            self.id = video_id
            self.title = video_data['title']
            self.link = f'https://youtube.com/watch?v={video_id}'
            self.views = video_data['views']
            self.like_count = video_data['like_count']
        except IndexError:
            # В случае ошибки при получении данных, инициализировать только video_id
            self.id = video_id
            self.title = None
            self.link = None
            self.views = None
            self.like_count = None

    def __str__(self):
        return self.title

    def _get_video_data(self, video_id):
        # Получение API-ключа из переменных окружения
        api_key = os.getenv('YT_API_KEY')

        # Создание YouTube API клиента
        api_service_name = "youtube"
        api_version = "v3"
        youtube = build(api_service_name, api_version, developerKey=api_key)

        # Запрос к YouTube API для получения данных о видео
        request = youtube.videos().list(
            part="snippet,statistics",
            id=video_id
        )
        response = request.execute()
        video_data = response['items'][0]['snippet']
        statistics = response['items'][0]['statistics']

        # Возвращение данных о видео
        return {
            'title': video_data['title'],
            'views': statistics['viewCount'],
            'like_count': statistics['likeCount'],

        }


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

        # Получение данных о плейлисте из API
        playlist_data = self._get_playlist_data(playlist_id)
        self.title = playlist_data['title']

    def _get_playlist_data(self, playlist_id):
        # Получение API-ключа из переменных окружения
        api_key = os.getenv('YT_API_KEY')

        # Создание YouTube API клиента
        api_service_name = "youtube"
        api_version = "v3"
        youtube = build(api_service_name, api_version, developerKey=api_key)

        # Запрос к YouTube API для получения данных о плейлисте
        request = youtube.playlists().list(
            part="snippet",
            id=playlist_id
        )
        response = request.execute()
        playlist_data = response['items'][0]['snippet']

        # Возвращение данных о плейлисте
        return {
            'title': playlist_data['title']
        }
