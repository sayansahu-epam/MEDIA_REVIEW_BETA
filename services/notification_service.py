from email.mime import message
from database.db_connection import get_connection



class NotificationService:
    """
    Handles notification logic for new reviews.
    """

    def __init__(self):
        self.observers = []
        self.notifications = {}

    def register_observer(self, observer):
        self.observers.append(observer)


    def notify_observers(self, media_id, message):
        """
        Stores notification in SQLite so it persists across runs.
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
        "INSERT INTO notifications (media_id, message) VALUES (?, ?)",
        (media_id, message)
        )

        conn.commit()
        conn.close()



    def get_notifications_for_media(self, media_id: int):
        """
        Fetches all notifications for a media_id from SQLite.
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT message FROM notifications WHERE media_id = ?",
            (media_id,)
    )

        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]


# Create a single shared instance
notification_service = NotificationService()
