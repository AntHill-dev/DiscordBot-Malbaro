from bot.database import main
from bot.database.models.user import User


class GetUserInfo:
    """Get user info by user id."""

    def get_user_info(self: "main.DatabaseMarlboro", user_id: int) -> User:
        """Get user info.

        Args:
            user_id: User id

        Returns:
            list: User info
        """
        result = self.execute("SELECT * FROM info WHERE ID = %s;", user_id)

        return User(
            id=user_id,
            messages_count=result[0][1],
            voice_time=result[0][2],
        ) if not result else User(
            id=user_id,
            messages_count=0,
            voice_time=0,
        )
