import os
from dataclasses import field
from typing import Final

from dotenv import load_dotenv

load_dotenv()


class APIKeyDiscordBot:
    """Storage for the bot's secret token."""

    TOKEN: Final[str] = field(default=os.environ.get("TOKEN", "!TOKEN"))


class CommandPrefixDiscordBot:
    """Storage for the bot's command prefix."""

    COMMAND_PREFIX: Final[str] = field(default=os.environ.get("COMMAND_PREFIX", "!COMMAND_PREFIX"))
