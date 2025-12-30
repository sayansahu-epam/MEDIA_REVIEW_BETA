from database.db_connection import get_connection


def add_review(review_id: int, user_id: int, media_id: int, rating: int, comment: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO reviews (review_id, user_id, media_id, rating, comment)
        VALUES (?, ?, ?, ?, ?)
        """,
        (review_id, user_id, media_id, rating, comment)
    )

    connection.commit()
    connection.close()


def get_reviews_for_media(media_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT review_id, user_id, rating, comment
        FROM reviews
        WHERE media_id = ?
        """,
        (media_id,)
    )

    results = cursor.fetchall()
    connection.close()
    return results
