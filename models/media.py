class Media:
    def __init__(self, media_id: int, title: str, media_type: str):
        self.media_id = media_id
        self.title = title
        self.media_type = media_type


class Movie(Media):
    def __init__(self, media_id: int, title: str):
        super().__init__(media_id, title, "movie")


class Series(Media):
    def __init__(self, media_id: int, title: str):
        super().__init__(media_id, title, "series")

#Song added explicitly
class Song(Media):
    def __init__(self, media_id: int, title: str):
        super().__init__(media_id, title, "song")
