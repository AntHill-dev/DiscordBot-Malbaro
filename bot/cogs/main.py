from bot.misc.types import BotType

usr_command_list = [
    "example",
]

general_cogs_list = [
    "events",
    "listeners",
    "user_info",
]


def setup_cogs_for_user(bot: BotType) -> None:
    """Registering user commands for a specific bot.

    Args:
        bot: Bot for which commands will be registered for the user
    """
    for cog in usr_command_list:
        bot.load_extension(f"bot.cogs.user.{cog}")


def setup_general_cogs(bot: BotType) -> None:
    """Registering general cogs for a specific bot.

    Args:
        bot: Bot for which commands will be registered for the user
    """
    for cog in general_cogs_list:
        bot.load_extension(f"bot.cogs.general.{cog}")
