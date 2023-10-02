from dataclasses import dataclass, field
from typing import Final

from bot.misc.env import APIKeyDiscordBot, CommandPrefixDiscordBot
from bot.misc.types import IntentsType
from bot.misc.utils import SingletonABC, get_default_msg_intents


class DefaultIntents:
    """Storage for the bot's intents."""

    INTENTS: Final[IntentsType] = field(default_factory=get_default_msg_intents)


@dataclass(frozen=True)
class BotConfig(metaclass=SingletonABC):
    """Bot configuration storage class.

    Attributes:
        TOKEN - A secret token for bot.
        INTENTS - A using intents for bot.
        COMMAND_PREFIX - A bot's command prefix.
    """

    TOKEN: str = APIKeyDiscordBot.TOKEN
    INTENTS: IntentsType = DefaultIntents.INTENTS
    COMMAND_PREFIX: str = CommandPrefixDiscordBot.COMMAND_PREFIX


Config = BotConfig()

StartUpParameters = {
    "command_prefix": Config.COMMAND_PREFIX,
    "intents": Config.INTENTS,
}
