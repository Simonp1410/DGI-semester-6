class Podcast_Episode:
    def __init__(self, title, artist, duration, guest) -> None:
        self.title = title
        self.artist = artist
        self.duration = duration
        self.guest = guest
        self.over_30_min = self.check_is_over_30_min(duration)
    def check_is_over_30_min(self, duration):
        return (duration>1800)
    def __str__(self) -> str:
        string_info = str(self.__dict__)
        return string_info
some_podcast= Podcast_Episode('Какая-то песняя', 'Кто-то', 123456, 'Кто-то другой')
print(some_podcast)