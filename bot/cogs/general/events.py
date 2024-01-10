import discord
import time

from discord.ext import commands
from discord.utils import get

from bot.misc.types import BotType
from bot.misc.config import EventsConfig
from bot.database.main import database

from loguru import logger


class CommandsEvents(commands.Cog):

    def __init__(self, bot: BotType) -> None:
        self.bot = bot

    # events in case of user call errors
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            logger.debug(
                f"{ctx.author.name} calls a non-existing command.")
            await ctx.reply(f" {ctx.author.name}, команда не найдена!")

        if isinstance(error, commands.MissingPermissions):
            logger.debug(
                f"{ctx.author.name} calls a command that he does not have rights to.")
            await ctx.reply(f" {ctx.author.name}, y вас недостаточно прав!")

        if isinstance(error, commands.MissingRequiredArgument):
            logger.debug(
                f"{ctx.author.name} member called the command and did not specify an argument.")
            await ctx.reply(f" {ctx.author.name}, введите аргументы!")

        if isinstance(error, commands.NotOwner):
            logger.debug(
                f"{ctx.author.name} member calls a command that only the bot owner has access to.")
            await ctx.reply(f" {ctx.author.name}, эту команду может использовать только владелец бота!")

    # events when launching the bot.
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for member in guild.members:
                if not database.execute("SELECT id FROM users WHERE id = %s", member.id):
                    database.execute(
                        "INSERT INTO users VALUES (%s, %s)", member.id, member.name, noreturn=True)
                    database.execute(
                        "INSERT INTO about VALUES (%s, %s)", member.id, "none", noreturn=True)
                    database.execute(
                        "INSERT INTO info VALUES (%s, %s, %s)", member.id, 0, 0, noreturn=True)

                    logger.debug(
                        f"{member} added to the database.")

        logger.debug("Bot is ready.")

    # events when a user joins the discord server.
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if not database.execute("SELECT id FROM users WHERE id = %s", member.id):
            database.execute(
                "INSERT INTO users VALUES (%s, %s)", member.id, member.name, noreturn=True)
            database.execute(
                "INSERT INTO about VALUES (%s, %s)", member.id, "none", noreturn=True)
            database.execute(
                "INSERT INTO info VALUES (%s, %s, %s)", member.id, 0, 0, noreturn=True)

            logger.debug(
                f"{member} added to the database.")
            logger.info(
                f"{member} joined the discord server.")

    # events during voice channel status updates.
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        role = member.guild.get_role(EventsConfig().voice_role)
        time_join = 0

        if after.channel and after.channel.type == discord.ChannelType.voice:
            await member.add_roles(role)
            logger.info(
                f"{member} joined the voice chat.")

            time_join = time.time()

        if not after.channel and before.channel.type == discord.ChannelType.voice:
            await member.remove_roles(role)
            logger.info(
                f"{member} has left the voice chat.")

            time_on_voice = time.time() - time_join
            database.execute(
                "UPDATE info SET voice_time = voice_time + %s WHERE id = %s", time_on_voice, member.id, noreturn=True)

    # events during user status updates.
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.roles != after.roles:
            role = [i for i in after.roles if i not in before.roles]
            logger.info(
                f"{before.name} got the role: {role}.")

    # event when writing a message.
    @commands.Cog.listener()
    async def on_message(self, message):
        database.execute(
            "UPDATE info SET messages = messages + 1 WHERE id = %s", message.author.id, noreturn=True)

        logger.info(
            f"{message.author} wrote this message: '{message.content}', on this chat: {message.channel.name}.")


def setup(bot: BotType) -> None:
    bot.add_cog(CommandsEvents(bot))
