import sqlite3
import os


DB_NAME = "media_review.db"
TEST_DB_NAME = "tests/test_media_review.db"

def get_connection():
    """
    Creates and returns a SQLite database connection.
    """
    if os.environ.get("PYTEST_RUNNING") == "1":
        connection = sqlite3.connect(
            TEST_DB_NAME,
            timeout=5,
            isolation_level=None
        )
    else:
        connection = sqlite3.connect(
            DB_NAME,
            isolation_level=None
        )

    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def create_tables():
    """
    Creates required tables if they do not already exist.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    media_id INTEGER NOT NULL,
    message TEXT NOT NULL
        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS media (
            media_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            media_type TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            review_id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            media_id INTEGER NOT NULL,
            rating INTEGER NOT NULL,
            comment TEXT,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (media_id) REFERENCES media(media_id)
        )
    """)

    connection.commit()
    connection.close()
