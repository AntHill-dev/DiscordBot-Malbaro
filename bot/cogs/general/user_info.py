import discord
from discord.ext import commands

from bot.database.main import database
from bot.database.models.user import User
from bot.misc.types import AppContext, BotType


class UserInfoCommand(commands.Cog):
    """The cog class of user info commands.

    Methods:
        userinfo(self, ctx: AppContext) -> None:
            User greeting command.
    """

    @discord.command(name="userinfo", description="Информация о пользователе")
    async def userinfo(
            self,
            ctx: AppContext,
            member: discord.Option(
                discord.Member,
                description="Пользователь",
            ),
        ) -> None:
        """User info command.

        Args:
            ctx: Context of command
            member: Member
        """
        user_info: User = database.get_user_info(member.id)

        embed = discord.Embed(
            title="Информация о пользователе",
            description="\n".join(
                (
                    f"Пользователь: @{member.nick or member.name}",
                    f"Общее кол-во смс: {user_info.messages_count}",
                    f"Время, проведенное в войсе: {user_info.voice_time}s (~{user_info.voice_time // 60}m)",
                ),
            ),
            color=discord.Color.green(),
        )
        embed._thumbnail = {"url": member.display_avatar.url} if member.display_avatar else None

        await ctx.respond(embed=embed)


def setup(bot: BotType) -> None:
    """Load function cog UserInfoCommand for bot.

    Args:
        bot: Bot for which cog will be loaded.
    """
    bot.add_cog(UserInfoCommand())
