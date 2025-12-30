from database.media_dao import (
    add_media as dao_add_media,
    get_all_media as dao_get_all_media,
    search_media_by_title as dao_search_media_by_title
)


def add_media(media_id: int, title: str, media_type: str):
    """
    Adds a new media item to the system.
    """
    dao_add_media(media_id, title, media_type)


def list_all_media():
    """
    Returns all media items.
    """
    return dao_get_all_media()


def search_media(title: str):
    """
    Searches media by title.
    """
    return dao_search_media_by_title(title)
