from database.user_dao import add_user as dao_add_user


def add_user(user_id: int, name: str):
    """
    Adds a new user to the system.
    """
    dao_add_user(user_id, name)


from database.user_dao import get_all_users as dao_get_all_users


def list_all_users():
    """
    Returns all users in the system.
    """
    return dao_get_all_users()
