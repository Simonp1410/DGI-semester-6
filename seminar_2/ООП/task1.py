class Song:
    def __init__(self,title,artist,release_year):
        self.a=title
        self.b =artist
        self.c=release_year
some_song= Song('Какая-то песняя', 'Кто-то', 2024)
print(some_song.b)