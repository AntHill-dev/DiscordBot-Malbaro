from .get_user_id import GetUserID
from .set_user_info import SetUserInfo


class Methods(
    GetUserID,
    SetUserInfo,
):
    """Database methods class.

    Methods:
        get_user_id_by_username(self: "main.DatabaseMalboro", username: str)
            Get user id by username.

        set_user_info(self: "main.DatabaseMalboro", user_id: int, messages: int, voice_time: int)
            Set user info by user id.
    """
