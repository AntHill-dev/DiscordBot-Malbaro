import logging
from typing import TypeAlias

from discord import ApplicationContext, Intents
from discord.ext import commands

IntentsType: TypeAlias = Intents
AppContext: TypeAlias = ApplicationContext
BotType: TypeAlias = commands.Bot
HandlerType: TypeAlias = logging.Handler
