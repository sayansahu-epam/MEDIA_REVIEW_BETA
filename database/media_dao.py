from database.db_connection import get_connection


def add_media(media_id: int, title: str, media_type: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO media (media_id, title, media_type) VALUES (?, ?, ?)",
        (media_id, title, media_type)
    )

    connection.commit()
    connection.close()


def get_all_media():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT media_id, title, media_type FROM media")
    results = cursor.fetchall()

    connection.close()
    return results


def search_media_by_title(title: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT media_id, title, media_type FROM media WHERE title LIKE ?",
        (f"%{title}%",)
    )

    results = cursor.fetchall()
    connection.close()
    return results
