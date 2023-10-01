from dataclasses import dataclass

from bot.misc.env import APIDiscordBot


@dataclass
class BotConfig:  # noqa: D101
    TOKEN = APIDiscordBot.TOKEN
    COMMAND_PREFIX = "!"
    INTENTS = APIDiscordBot.INTENTS
