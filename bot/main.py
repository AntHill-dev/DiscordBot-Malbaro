from discord.ext import commands

from bot.cogs.main import setup_cogs_for_user
from bot.misc.config import Config, StartUpParameters
from bot.misc.utils import SingletonABC


class BotMarlboro(commands.Bot, metaclass=SingletonABC):
    """Main bot class.

    Methods:
        _command_registration(self, /) -> None:
            Logs all commands for user and administrator (cogs)

        run(self, /) -> None:
            Start a bot using a secret token.
    """

    def __init__(self, *args, **kwargs) -> None:  # type: ignore
        super().__init__(*args, **kwargs)
        self._command_registration()

    def _command_registration(self) -> None:
        setup_cogs_for_user(self)

    def run(self) -> None:
        """Start a bot using a secret token."""
        super().run(Config.TOKEN)


bot = BotMarlboro(**StartUpParameters)
