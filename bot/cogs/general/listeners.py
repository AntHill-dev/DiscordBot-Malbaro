import asyncio
import time

import discord
from discord.ext import commands
from loguru import logger

from bot.database.main import database
from bot.misc.config import config
from bot.misc.types import BotType
from bot.misc.views.private_voice_controller import PrivateVoiceControllerView


class Listeners(commands.Cog):
    """The cog class of listeners."""

    def __init__(self, bot: BotType) -> None:
        self.bot: BotType = bot

        self._voice_listener: dict[str, float] = {}
        self._private_channels: dict[int, discord.VoiceChannel] = {}


    @commands.Cog.listener(name="on_ready")
    async def on_ready(self) -> None:
        self._loop_task = asyncio.ensure_future(self._loop(), loop=self.bot.loop)

        self.bot.add_view(PrivateVoiceControllerView(self))

        logger.info("[Listener] Bot is ready")


    async def get_voice_channel_by_id(self, id: int) -> discord.VoiceChannel:
        voices = self.bot.get_guild(config.bot.discord_guild_id).voice_channels

        for voice in voices:
            if voice.id == id:
                return voice

        return None


    async def _loop(self) -> None:
        while True:
            for user, spent_time in self._voice_listener.copy().items():
                now_time = time.monotonic()
                time_in_seconds = int(now_time - spent_time)

                user_info = database.get_user_info(user)
                user_info.voice_time += time_in_seconds

                database.set_user_info(user_info)

                self._voice_listener[user] = now_time
            await asyncio.sleep(1)


    @commands.Cog.listener(name="on_message")
    async def message_listener(self, message: discord.Message) -> None:
        if message.guild and message.guild.name != "AntHiLL" or message.author and message.author.bot:
            return

        user_info = database.get_user_info(message.author.id)
        user_info.messages_count += 1
        database.set_user_info(user_info)
        logger.info(f"[Listener] User <{message.author.name}> sent message in channel <{message.channel.name}>")


        if message.content == "WHAT?":
            await message.channel.send(
                embed=discord.Embed(
                    title="Настройка приватных голосовых каналов",
                    description="Настрой свой приватный голосовой канал легко и быстро!",
                    color=discord.Color.green(),
                ),
                view=PrivateVoiceControllerView(self),
            )


    async def _private_user_voice_channel(self, member: discord.Member) -> discord.TextChannel:
        if not self._private_channels.get(member.id):
            channel = await next(
                category
                for category in member.guild.categories
                if "PRIVATE" in category.name.upper()
            ).create_voice_channel(
                name=member.name,
                overwrites={
                    member: discord.PermissionOverwrite(administrator=True),
                },
                user_limit=1,
            )
            self._private_channels[member.id] = channel.id

        return await self.get_voice_channel_by_id(self._private_channels[member.id])


    async def _check_for_private_user_voice_channel(
            self,
            member: discord.Member,
            before: discord.VoiceState,
            after: discord.VoiceState,
    ) -> None:
        if after.channel and after.channel.name == "[+] Create private":
            private_voice_channel = await self._private_user_voice_channel(member)
            await member.move_to(private_voice_channel)
        elif before.channel and before.channel.id == self._private_channels.get(member.id, 0):
            await before.channel.delete()
            del self._private_channels[member.id]


    @commands.Cog.listener(name="on_voice_state_update")
    async def voice_listener(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if member.guild.name != "AntHiLL":
            return

        await self._check_for_private_user_voice_channel(member, before, after)

        if not before.channel and after.channel:
            state = f"- >>> CHANNEL <{after.channel.name}>"
            self._voice_listener[member.id] = time.monotonic()
            self._loop_task.cancel()
            self._loop_task = asyncio.ensure_future(self._loop())
        elif before.channel and not after.channel:
            state = f"CHANNEL <{before.channel.name}> >>> LEFT"

            if member.id in self._voice_listener:
                time_in_seconds = int(time.monotonic() - self._voice_listener.pop(member.id))
                user_info = database.get_user_info(member.id)
                user_info.voice_time += time_in_seconds
                database.set_user_info(user_info)
                self._loop_task.cancel()
                self._loop_task = asyncio.ensure_future(self._loop())
        else:
            state = f"CHANNEL <{before.channel.name}> >>> CHANNEL <{after.channel.name}>"

        logger.info(f"[Listener] User <{member.name}> changed voice state: {state}")


def setup(bot: BotType) -> None:
    """Load function cog Listeners for bot.

    Args:
        bot: Bot for which cog will be loaded.
    """
    bot.add_cog(Listeners(bot))
