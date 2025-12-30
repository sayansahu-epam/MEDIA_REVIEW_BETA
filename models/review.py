class Review:
    def __init__(
        self,
        review_id: int,
        user_id: int,
        media_id: int,
        rating: int,
        comment: str
    ):
        self.review_id = review_id
        self.user_id = user_id
        self.media_id = media_id
        self.rating = rating
        self.comment = comment
