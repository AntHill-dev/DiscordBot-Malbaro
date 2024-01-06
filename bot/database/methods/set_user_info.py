import psycopg2.sql

from bot.database import main
from bot.database.models.user import User


class SetUserInfo:
    """Set user info by user id."""

    def set_user_info(
            self: "main.DatabaseMarlboro",
            user: User,
    ) -> None:
        """Set user info.

        Args:
            user: User

        Returns:
            None
        """
        self.execute(
            psycopg2.sql.SQL(
                """
                INSERT INTO info (id, messages, voice_time)
                VALUES (%s, %s, %s)
                ON CONFLICT (id) DO UPDATE
                SET messages = excluded.messages, voice_time = excluded.voice_time
                """,
            ), user.id, user.messages_count, user.voice_time, noreturn=True,
        )
