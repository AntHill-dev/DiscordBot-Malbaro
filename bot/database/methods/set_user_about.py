import psycopg2.sql

from bot.database import main


class SetUserAbout:
    """Set user about by user id."""

    def set_user_about(
            self: "main.DatabaseMalboro",
            user_id: int,
            about: str,
    ) -> None:
        """Set user about.

        Args:
            user_id: User id
            about: About

        Returns:
            None
        """
        self.execute(
            psycopg2.sql.SQL(
                """
                INSERT INTO about (id, about)
                VALUES (%s, %s)
                ON CONFLICT (id) DO UPDATE
                SET about = excluded.about
                """,
            ), user_id, about, noreturn=True,
        )
