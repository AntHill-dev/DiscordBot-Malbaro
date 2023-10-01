import os
from dataclasses import field
from typing import Final

from dotenv import load_dotenv

from bot.misc.utils import SingletonABC

load_dotenv()


class APIKeyDiscordBot(SingletonABC):
    TOKEN: Final[str] = field(default=os.environ.get("TOKEN", "TOKEN not found"))


class CommandPrefixDiscordBot(SingletonABC):
    COMMAND_PREFIX: Final[str] = field(default=os.environ.get("COMMAND_PREFIX", "COMMAND_PREFIX not found"))

