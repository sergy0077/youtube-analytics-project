class Video:
    def __init__(self, video_id):
        # Инициализация атрибутов экземпляра класса Video
        self.id = video_id
        self.title = 'GIL в Python: зачем он нужен и как с этим жить'
        self.link = f'https://youtube.com/watch?v={video_id}'
        self.views = 1000
        self.likes = 500

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
        self.title = 'MoscowPython Meetup 78 - вступление'


