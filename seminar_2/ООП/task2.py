class Song:
    def __init__(self,title,artist,release_year) -> None:
        self.a=title
        self.b =artist
        self.c=release_year
    def get_info(self):
        info = {"title":self.a,
                "artist":self.b,
                "release_year":self.c}
        return info
some_song = Song('Какая-то песняя', 'Кто-то', 2024)
print(some_song.get_info())