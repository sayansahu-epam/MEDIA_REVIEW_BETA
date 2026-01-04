# from models.media import Media


# class MediaFactory:
#     """
#     Factory class to create Media objects based on media type.
#     """

#     @staticmethod
#     def create_media(media_id: int, title: str, media_type: str) -> Media:
#         if media_type == "movie":
#             return Media(media_id, title, "movie")

#         elif media_type == "web_show":
#             return Media(media_id, title, "web_show")

#         elif media_type == "song":
#             return Media(media_id, title, "song")

#         else:
#             raise ValueError(f"Unknown media type: {media_type}")


# patterns/media_factory.py



from models.media import Media, Movie, Series, Song



class MediaFactory:
    @staticmethod
    def create_media(media_id: int, title: str, media_type: str):
        media_type = media_type.lower()

        if media_type == "movie":
            return Movie(media_id, title)

        elif media_type == "series":
            return Series(media_id, title)
        
        
        elif media_type == "song":
            return Song(media_id, title)

        else:
            # Fallback for unknown types
            return Media(media_id, title, media_type)
