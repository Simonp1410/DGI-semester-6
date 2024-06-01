class Song:
    def __init__(self,title, artist, release_year):
        self.title=title
        self.artist =artist
        self.release_year=release_year
    def __str__(self) -> str:
        string_info = str(self.__dict__)
        return string_info
some_song= Song('Какая-то песняя', 'Кто-то', 2024)
print(some_song)