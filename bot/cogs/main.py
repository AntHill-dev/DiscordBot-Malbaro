from bot.misc.types import BotType

usr_command_list = [
    "example",
]


def setup_cogs_for_user(bot: BotType) -> None:
    """Registering user commands for a specific bot.

    Args:
        bot: Bot for which commands will be registered for the user
    """
    for cog in usr_command_list:
        bot.load_extension(f"bot.cogs.user.{cog}")
