class NotificationService:
    """
    Handles notification logic for new reviews.
    """

    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, media_id: int, review_info: str):
        for observer in self._observers:
            observer.update(media_id, review_info)


# Create a single shared instance
notification_service = NotificationService()
