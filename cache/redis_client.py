import redis


def get_redis_client():
    """
    Creates and returns a Redis client.
    Returns None if Redis is not available.
    """
    try:
        client = redis.Redis(
            host="localhost",
            port=6379,
            decode_responses=True
        )
        client.ping()
        return client
    except redis.RedisError:
        return None
