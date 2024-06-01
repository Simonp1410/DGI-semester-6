class Audio_Item:
    def __init__(self, title, artist, is_liked=False) -> None:
        self.title=title
        self.artist =artist
        self.is_liked = is_liked
    def like(self):
        return not self.is_liked
        
class Song(Audio_Item):
    def __init__(self, title, artist, release_year) -> None:
        super().__init__(title, artist)
        self.release_year = release_year
    def __str__(self) -> str:
        string_info = str(self.__dict__)
        return string_info

        
class Podcast_Episode(Audio_Item):
    def __init__(self, title, artist, duration, guest) -> None:
        super().__init__(title, artist)
        self.duration = duration
        self.guest = guest
        self.over_30_min = self.check_is_over_30_min(duration)
    def check_is_over_30_min(self, duration):
        return (duration>1800)
    def __str__(self) -> str:
        string_info = str(self.__dict__)
        return string_info

some_song= Song('Какая-то песняя', 'Кто-то', 2024)
print(some_song)
some_podcast= Podcast_Episode('Какая-то песняя', 'Кто-то', 123, 'Кто-то другой')
print(some_podcast)