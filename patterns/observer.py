from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Abstract Observer interface.
    """

    @abstractmethod
    def update(self, media_id: int, review_info: str):
        pass


class UserObserver(Observer):
    """
    Concrete Observer representing a user.
    """

    def __init__(self, user_name: str):
        self.user_name = user_name

    def update(self, media_id: int, review_info: str):
        print(
            f"Notification for {self.user_name}: "
            f"New review added for media {media_id} - {review_info}"
        )
