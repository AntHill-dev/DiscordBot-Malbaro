from discord.ext import commands

from bot.cogs.general import help
from bot.cogs.main import setup_cogs_for_user, setup_general_cogs
from bot.misc.config import config
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

        attributes_for_help = {
            "name": "help",
            "aliases": ["helpme"],
            "cooldown": commands.CooldownMapping.from_cooldown(3, 5, commands.BucketType.user),
        }

        self.help_command = help.MarlboroHelpCommand(command_attrs=attributes_for_help)
        self._command_registration()

    def _command_registration(self) -> None:
        setup_cogs_for_user(self)
        setup_general_cogs(self)

    def run(self) -> None:
        """Start a bot using a secret token."""
        super().run(config.bot.token)
