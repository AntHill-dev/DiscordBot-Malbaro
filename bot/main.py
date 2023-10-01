from discord.ext import commands

from bot.cogs.main import setup_cogs_for_user
from bot.misc.config import BotConfig
from bot.misc.utils import SingletonABC


class BotMarlboro(commands.Bot, SingletonABC):
    def __init__(self) -> None:
        super().__init__(command_prefix=BotConfig.COMMAND_PREFIX, intents=BotConfig.INTENTS)

    def run(self) -> None:
        super().run(BotConfig.TOKEN)


bot = BotMarlboro()

setup_cogs_for_user(bot)
