from bot.misc.types import BotType

usr_command_list = [
    "example",
]


def setup_cogs_for_user(bot: BotType):
    for cog in usr_command_list:
        bot.load_extension(f"user.{cog}")
