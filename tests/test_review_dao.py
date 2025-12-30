from database.review_dao import add_review
from database.user_dao import add_user
from database.media_dao import add_media
from database.review_dao import get_reviews_for_media

import sqlite3
import pytest
from database.review_dao import add_review
from database.media_dao import add_media



def test_add_review():
    # Arrange
    add_user(1, "Alice")
    add_media(1, "Inception", "movie")

    # Act
    add_review(1, 1, 1, 5, "Great movie!")
    reviews = get_reviews_for_media(1)
    assert len(reviews) == 1
    assert reviews[0][0] == 1        # review_id
    assert reviews[0][1] == 1        # user_id
    assert reviews[0][2] == 5        # rating
    assert reviews[0][3] == "Great movie!"



def test_add_review_fails_when_user_missing():
    # Arrange
    add_media(1, "Inception", "movie")  # media exists, user does not

    # Act + Assert
    with pytest.raises(sqlite3.IntegrityError):
        add_review(1, 999, 1, 5, "Should fail")
        
        
def test_add_review_fails_when_media_missing():
    # Arrange
    add_user(1, "Alice")  # user exists, media does not

    # Act + Assert
    with pytest.raises(sqlite3.IntegrityError):
        add_review(1, 1, 999, 5, "Should fail")




def test_add_review_duplicate_id_raises_error():
    # Arrange
    add_user(1, "Alice")
    add_media(1, "Inception", "movie")
    add_review(1, 1, 1, 5, "First review")

    # Act + Assert
    with pytest.raises(sqlite3.IntegrityError):
        add_review(1, 1, 1, 4, "Duplicate review ID")
