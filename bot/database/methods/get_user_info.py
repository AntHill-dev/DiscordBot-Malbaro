from bot.database import main


class GetUserInfo:
    """Get user info by user id."""

    def get_user_info(self: "main.DatabaseMarlboro", user_id: int) -> list:
        """Get user info.

        Args:
            user_id: User id

        Returns:
            list: User info
        """
        return self.execute("SELECT * FROM info WHERE ID = %s;", user_id)
