from database.media_dao import add_media
from database.media_dao import get_all_media
from database.media_dao import search_media_by_title

import sqlite3
import pytest


def test_create_media():
    # Arrange
    media_id = 1
    title = "Inception"
    media_type = "movie"

    # Act
    add_media(media_id, title, media_type)
    media = get_all_media()

    # Assert
    assert len(media) == 1
    assert media[0][0] == media_id
    assert media[0][1] == title
    assert media[0][2] == media_type


def test_search_media_by_title():
    # Arrange
    add_media(1, "Inception", "movie")
    add_media(2, "Interstellar", "movie")

    # Act
    results = search_media_by_title("Inception")

    # Assert
    assert len(results) == 1
    assert results[0][1] == "Inception"



def test_add_media_duplicate_id_raises_error():
    # Arrange
    add_media(1, "Inception", "movie")

    # Act + Assert
    with pytest.raises(sqlite3.IntegrityError):
        add_media(1, "Inception Again", "movie")
