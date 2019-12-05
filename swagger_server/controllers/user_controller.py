import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def app_create_user(body):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def app_create_users_with_array_input(body):  # noqa: E501
    """Creates list of users with given input array

     # noqa: E501

    :param body: List of user object
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [User.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def app_create_users_with_list_input(body):  # noqa: E501
    """Creates list of users with given input array

     # noqa: E501

    :param body: List of user object
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [User.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def app_delete_user(username):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be deleted
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def app_get_user_by_name(username):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing.
    :type username: str

    :rtype: User
    """
    return 'do some magic!'


def app_login_user(username, password):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    return 'do some magic!'


def app_logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def app_mark_word_learned(username, word_id):  # noqa: E501
    """Update word status for the user

    This can only be done by the logged in user. # noqa: E501

    :param username: name that need to be updated
    :type username: str
    :param word_id: ID of word to update
    :type word_id: int

    :rtype: None
    """
    return 'do some magic!'


def app_update_user(body, username):  # noqa: E501
    """Updated user

    This can only be done by the logged in user. # noqa: E501

    :param body: Updated user object
    :type body: dict | bytes
    :param username: name that need to be updated
    :type username: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
