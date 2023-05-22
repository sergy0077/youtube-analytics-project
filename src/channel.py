import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = None
        self.description = None
        self.url = None
        self.subscriber_count = None
        self.video_count = None
        self.view_count = None

        self._fetch_channel_info()

    def _fetch_channel_info(self) -> None:
        """Получает информацию о канале через YouTube API и заполняет атрибуты экземпляра."""
        response = self.youtube.channels().list(id=self.channel_id, part='snippet, statistics').execute()
        if 'items' in response:
            channel_info = response['items'][0]
            self.title = channel_info['snippet']['title']
            self.description = channel_info['snippet']['description']
            self.url = f"https://www.youtube.com/channel/{self.channel_id}"
            self.subscriber_count = int(channel_info['statistics']['subscriberCount'])
            self.video_count = int(channel_info['statistics']['videoCount'])
            self.view_count = int(channel_info['statistics']['viewCount'])

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API."""
        return cls.youtube

    def to_json(self, filename: str) -> None:
        """Сохраняет значения атрибутов экземпляра в файл в формате JSON."""
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open(filename, 'w') as file:
            json.dump(data, file)


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(
            json.dumps(self.youtube.channels().list(id=self.channel_id, part='snippet, statistics').execute(), indent=2,
                       ensure_ascii=False))
