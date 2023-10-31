from .get_user_about import GetUserAbout
from .get_user_id import GetUserID
from .get_user_info import GetUserInfo
from .set_user_about import SetUserAbout
from .set_user_info import SetUserInfo


class Methods(
    GetUserAbout,
    GetUserID,
    GetUserInfo,
    SetUserAbout,
    SetUserInfo,
):
    """Database methods class.

    Methods:
        get_user_id_by_username(self: "main.DatabaseMalboro", username: str) -> int
            Get user id by username.

        get_user_about(self: "main.DatabaseMalboro", user_id: int) -> str
            Get user about by user id.

        get_user_info(self: "main.DatabaseMalboro", user_id: int) -> list
            Get user info by user id.

        set_user_about(self: "main.DatabaseMalboro", user_id: int, about: str) -> None
            Set user about by user id.

        set_user_info(self: "main.DatabaseMalboro", user_id: int, messages: int, voice_time: int) -> None
            Set user info by user id.
    """
