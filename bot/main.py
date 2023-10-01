from discord.ext import commands
from loguru import logger

from bot.misc.config import BotConfig


class BotMarlboro(commands.Bot):  # noqa: D101
    def __init__(self) -> None:  # noqa: D107
        super().__init__(command_prefix=BotConfig.COMMAND_PREFIX, intents=BotConfig.INTENTS)

    def run(self) -> None:  # noqa: D102
        super().run(BotConfig.TOKEN)


bot = BotMarlboro()
