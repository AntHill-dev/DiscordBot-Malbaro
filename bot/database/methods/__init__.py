from .get_user_about import GetUserAbout
from .get_user_info import GetUserInfo
from .set_user_about import SetUserAbout
from .set_user_info import SetUserInfo


class Methods(
    GetUserAbout,
    GetUserInfo,
    SetUserAbout,
    SetUserInfo,
):
    """Database methods class.

    Methods:
        get_user_about(self: "main.DatabaseMarlboro", user_id: int) -> str
            Get user about by id.

        get_user_info(self: "main.DatabaseMarlboro", user_id: int) -> bot.database.models.user.User
            Get user info by id.

        set_user_about(self: "main.DatabaseMarlboro", user_id: int, about: str) -> None
            Set user about by id.

        set_user_info(self: "main.DatabaseMarlboro", user: bot.database.models.user.User) -> None
            Set user info.
    """
