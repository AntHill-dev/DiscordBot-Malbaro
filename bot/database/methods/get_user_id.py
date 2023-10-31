import psycopg2.sql

from bot.database import main


class GetUserID:
    """Get user id by username."""

    def get_user_id_by_username(self: "main.DatabaseMalboro", username: str) -> int:
        """Get user id by username.

        Args:
            username: Username

        Returns:
            int: User id
        """
        result = self.execute(
            psycopg2.sql.SQL(
                """
                INSERT INTO users (username)
                VALUES (%s)
                ON CONFLICT (username) DO UPDATE
                SET username = excluded.username
                RETURNING id
                """,
            ), username,
        )
        return result[0][0] if len(result) == 1 else result[1][0]
