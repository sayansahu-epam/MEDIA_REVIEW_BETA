from database.media_dao import get_all_media
from database.review_dao import get_reviews_for_media
from database.db_connection import get_connection


def get_recommendations_for_user(user_id: int):
    """
    Recommends media items that the user has not reviewed yet.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT DISTINCT media_id FROM reviews WHERE user_id = ?",
        (user_id,)
    )
    reviewed_media = {row[0] for row in cursor.fetchall()}
    connection.close()

    all_media = get_all_media()

    recommendations = [
        media for media in all_media if media[0] not in reviewed_media
    ]

    return recommendations



from database.db_connection import get_connection


def get_top_rated_media():
    """
    Returns media sorted by highest average rating.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT m.media_id, m.title, m.media_type, AVG(r.rating) as avg_rating
        FROM media m
        JOIN reviews r ON m.media_id = r.media_id
        GROUP BY m.media_id
        ORDER BY avg_rating DESC
    """)

    results = cursor.fetchall()
    connection.close()
    return results
