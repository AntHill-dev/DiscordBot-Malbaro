from bot.database import main


class GetUserAbout:
    """Get user about by user id."""

    def get_user_about(self: "main.DatabaseMarlboro", user_id: int) -> str:
        """Get user about.

        Args:
            user_id: User id

        Returns:
            str: About
        """
        return (
            self.execute("SELECT about FROM about WHERE ID = %s;", user_id) or [[user_id, "No info"]]
        )[0][1]
