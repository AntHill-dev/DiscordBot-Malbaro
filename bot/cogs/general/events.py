from discord.ext import commands

from bot.misc.types import BotType


class CommandsEvents(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f" {ctx.author.name} , команда не найдена!")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f" {ctx.author.name} , y вас недостаточно прав!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f" {ctx.author.name} , введите аргументы!")


def setup(bot: BotType) -> None:
    bot.add_cog(CommandsEvents())
