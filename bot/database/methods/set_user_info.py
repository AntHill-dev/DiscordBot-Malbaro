import psycopg2.sql

from bot.database import main


class SetUserInfo:
    """Set user info by user id."""

    def set_user_info(
            self: "main.DatabaseMarlboro",
            user_id: int,
            messages: int,
            voice_time: int,
    ) -> None:
        """Set user info.

        Args:
            user_id: User id
            messages: Messages count
            voice_time: Voice time

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
            ), user_id, messages, voice_time, noreturn=True,
        )
