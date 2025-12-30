import sys
from pathlib import Path

import os

os.environ["PYTEST_RUNNING"] = "1"


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


from database.db_connection import create_tables

create_tables()



import pytest
from database.db_connection import get_connection

@pytest.fixture(autouse=True)
def clear_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM reviews")
    cursor.execute("DELETE FROM media")
    cursor.execute("DELETE FROM users")

    connection.commit()
    connection.close()
