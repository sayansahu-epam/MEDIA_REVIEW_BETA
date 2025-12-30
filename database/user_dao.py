from database.db_connection import get_connection


def add_user(user_id: int, name: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO users (user_id, name) VALUES (?, ?)",
        (user_id, name)
    )

    connection.commit()
    connection.close()


def get_user_by_id(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT user_id, name FROM users WHERE user_id = ?",
        (user_id,)
    )

    result = cursor.fetchone()
    connection.close()
    return result

def get_all_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT user_id, name FROM users")
    results = cursor.fetchall()

    connection.close()
    return results

