import discord
from discord.ext import commands

from bot.misc.types import AppContext, BotType


class TestSlashCommand(commands.Cog):
    """The cog class of example commands.

    Methods:
        hello(self, ctx: AppContext) -> None:
            User greeting command.
    """

    @discord.command(name="hello", description="Приветствие!")
    async def hello(self, ctx: AppContext) -> None:
        """Hello user slash command.

        Args:
            ctx: All context when calling a command.
        """
        await ctx.respond(f"Hello, {ctx.author.name}")


def setup(bot: BotType) -> None:
    """Load function cog ExampleCommand for bot.

    Args:
        bot: Bot for which cog will be loaded.
    """
    bot.add_cog(TestSlashCommand())
