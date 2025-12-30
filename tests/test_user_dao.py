import os
import database.db_connection as db
from database.user_dao import add_user, get_user_by_id
from database.user_dao import add_user
from database.user_dao import get_user_by_id
from database.user_dao import get_all_users
import sqlite3
import pytest





# def setup_module():
#     """
#     Runs once before tests in this file.
#     Switches to a test database and creates tables.
#     """
#     db.DB_NAME = "test_media_review.db"
#     db.create_tables()


# def teardown_module():
#     """
#     Runs once after tests in this file.
#     Deletes the test database.
#     """
#     if os.path.exists("test_media_review.db"):
#         os.remove("test_media_review.db")

def test_add_and_get_user():
    # Arrange
    user_id = 100
    name = "TestUser"

    # Act
    add_user(user_id, name)
    user = get_user_by_id(user_id)

    # Assert
    assert user is not None
    assert user[0] == user_id
    assert user[1] == name
    
    
def test_get_all_users():
    # Arrange
    add_user(1, "Alice")
    add_user(2, "Bob")

    # Act
    users = get_all_users()

    # Assert
    assert len(users) == 2
    assert (1, "Alice") in users
    assert (2, "Bob") in users
    
    
def test_add_user_duplicate_id_raises_error():
    # Arrange
    add_user(1, "Alice")

    # Act + Assert
    with pytest.raises(sqlite3.IntegrityError):
        add_user(1, "Alice Again")


    
    
    
    
def test_create_user():
    
    add_user(1, "Test User")

