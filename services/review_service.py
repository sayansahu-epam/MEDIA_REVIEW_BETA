from utils.thread_manager import run_in_threads

from cache.review_cache import (
    get_cached_reviews,
    set_cached_reviews
)



from database.review_dao import (
    add_review as dao_add_review,
    get_reviews_for_media as dao_get_reviews_for_media
)

from services.notification_service import notification_service


def _add_review_internal(review_id, user_id, media_id, rating, comment):
    dao_add_review(review_id, user_id, media_id, rating, comment)

    review_info = f"Rating: {rating}, Comment: {comment}"
    notification_service.notify_observers(media_id, review_info)


def add_review(
    review_id: int,
    user_id: int,
    media_id: int,
    rating: int,
    comment: str
):
    """
    Adds a new review using multithreading.
    """
    run_in_threads(
        _add_review_internal,
        [(review_id, user_id, media_id, rating, comment)]
    )

def get_reviews_for_media(media_id: int):
    """
    Retrieves reviews for a media item using Redis cache if available.
    """
    cached_reviews = get_cached_reviews(media_id)
    if cached_reviews is not None:
        return cached_reviews

    reviews = dao_get_reviews_for_media(media_id)
    set_cached_reviews(media_id, reviews)
    return reviews
