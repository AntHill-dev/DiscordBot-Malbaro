import os
from typing import Final

from discord import Intents
from dotenv import load_dotenv

load_dotenv()


class APIDiscordBot:
    TOKEN: Final[str] = os.environ.get("TOKEN", "Token not found")
    INTENTS = Intents.default()

APIDiscordBot.INTENTS.message_content = True
