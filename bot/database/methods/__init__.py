from .get_user_id import GetUserID
from .set_user_about import SetUserAbout
from .set_user_info import SetUserInfo


class Methods(
    GetUserID,
    SetUserAbout,
    SetUserInfo,
):
    """Database methods class.

    Methods:
        get_user_id_by_username(self: "main.DatabaseMalboro", username: str)
            Get user id by username.

        set_user_about(self: "main.DatabaseMalboro", user_id: int, about: str)
            Set user about by user id.

        set_user_info(self: "main.DatabaseMalboro", user_id: int, messages: int, voice_time: int)
            Set user info by user id.
    """
