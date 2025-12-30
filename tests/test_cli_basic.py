import subprocess
import sys
from database.user_dao import get_user_by_id
from database.media_dao import get_all_media









def test_cli_add_user_runs():
    result = subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--add-user",
            "1",
            "Alice"
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "User added successfully." in result.stdout

    user = get_user_by_id(1)
    assert user is not None
    assert user[0] == 1
    assert user[1] == "Alice"




def test_cli_list_users():
    # Arrange: add one user via CLI
    subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--add-user",
            "2",
            "Bob"
        ],
        capture_output=True,
        text=True
    )

    # Act: list users
    result = subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--list-users"
        ],
        capture_output=True,
        text=True
    )

    # Assert
    assert result.returncode == 0
    assert "[2] Bob" in result.stdout





def test_cli_add_media():
    result = subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--add-media",
            "1",
            "Inception",
            "movie"
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Media added successfully." in result.stdout

    media = get_all_media()
    assert len(media) == 1
    assert media[0][0] == 1
    assert media[0][1] == "Inception"
    assert media[0][2] == "movie"



def test_cli_list_media():
    # Arrange: add one media item via CLI
    subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--add-media",
            "2",
            "Interstellar",
            "movie"
        ],
        capture_output=True,
        text=True
    )

    # Act: list media
    result = subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--list"
        ],
        capture_output=True,
        text=True
    )

    # Assert
    assert result.returncode == 0
    assert "[2] Interstellar (movie)" in result.stdout









def test_cli_search_media():
    # Arrange: add two media items
    subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--add-media",
            "3",
            "Avatar",
            "movie"
        ],
        capture_output=True,
        text=True
    )

    subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--add-media",
            "4",
            "Titanic",
            "movie"
        ],
        capture_output=True,
        text=True
    )

    # Act: search for one title
    result = subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--search",
            "Avatar"
        ],
        capture_output=True,
        text=True
    )

    # Assert
    assert result.returncode == 0
    assert "[3] Avatar (movie)" in result.stdout






def test_cli_add_review():
    # Arrange: add user
    subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--add-user",
            "10",
            "Charlie"
        ],
        capture_output=True,
        text=True
    )

    # Arrange: add media
    subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--add-media",
            "10",
            "Matrix",
            "movie"
        ],
        capture_output=True,
        text=True
    )

    # Act: add review
    result = subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--review",
            "10",      # USER_ID
            "10",      # MEDIA_ID
            "5",       # RATING
            "Amazing"  # COMMENT
        ],
        capture_output=True,
        text=True
    )

    # Assert
    assert result.returncode == 0
    assert "Review added successfully." in result.stdout







def test_cli_list_reviews_for_media():
    # Arrange: add user
    subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--add-user",
            "20",
            "Dave"
        ],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    # Arrange: add media
    subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--add-media",
            "20",
            "Gladiator",
            "movie"
        ],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    # Arrange: add review
    subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--review",
            "20",
            "20",
            "5",
            "Epic"
        ],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    # Act: list reviews
    
    result = subprocess.run(
        [
            sys.executable,
            "media_review.py",
            "--reviews",
            "20"
        ],
        capture_output=True,
        text=True,
        encoding="utf-8"
        
    )

    # Assert
    assert result.returncode == 0
    assert "Reviews for media ID 20:" in result.stdout
    assert "User 20 → Rating: 5 | Epic" in result.stdout
