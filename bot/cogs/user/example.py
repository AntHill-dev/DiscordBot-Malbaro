import discord
from discord.ext import commands

from bot.misc.types import AppContext, BotType


class ExampleCommands(commands.Cog):
    bot: BotType

    def __init__(self, bot: BotType) -> None:
        self.bot = bot

    @discord.command(name="hello", description="Приветствие!")
    async def hello(self, ctx: AppContext) -> None:
        await ctx.respond(f"Hello, {ctx.author.name}")
