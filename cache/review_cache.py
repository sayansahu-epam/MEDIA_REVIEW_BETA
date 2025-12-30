import json
from cache.redis_client import get_redis_client


def get_cached_reviews(media_id: int):
    """
    Retrieves cached reviews for a media item.
    Returns None if not found or Redis unavailable.
    """
    client = get_redis_client()
    if not client:
        return None

    key = f"media_reviews:{media_id}"
    cached_data = client.get(key)

    if cached_data:
        return json.loads(cached_data)

    return None


def set_cached_reviews(media_id: int, reviews):
    """
    Stores reviews for a media item in Redis cache.
    """
    client = get_redis_client()
    if not client:
        return

    key = f"media_reviews:{media_id}"
    client.set(key, json.dumps(reviews))
