from collections.abc import Sequence
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

from bot.misc.types import HandlerType, IntentsType
from bot.misc.utils import get_default_msg_intents, get_handlers_for_filtered

load_dotenv()
env_location = Path(".env").resolve()


class ConfigBD(BaseSettings):
    """Config for control BD."""

    class Config:  # noqa: D106
        case_sensitive = True
        env_prefix = "BD_"
        _env_file = env_location
        _env_file_encoding = "utf-8"


class BotConfig(BaseSettings):
    """Bot configuration storage class.

    Attributes:
        token - A secret token for bot.
        intents - A using intents for bot.
        command_prefix - A bot's command prefix.
    """
    token: str
    command_prefix: str
    intents: IntentsType = Field(default_factory=get_default_msg_intents)

    class Config:  # noqa: D106
        case_sensitive = True
        env_prefix = "BOT_"
        _env_file = env_location
        _env_file_encoding = "utf-8"


class BaseLoggingConfig(BaseSettings):
    """Base logging config."""
    level: int = 0
    force: bool = True
    handlers: Sequence[HandlerType] = Field(default_factory=get_handlers_for_filtered)

    class Config:  # noqa: D106
        case_sensitive = True
        env_prefix = "LOG_"
        _env_file = env_location
        _env_file_encoding = "utf-8"


class LoggingConfig(BaseModel):
    """Initialization class for logging."""
    base: BaseLoggingConfig = Field(default_factory=BaseLoggingConfig)
    format_output: str = "{time} | {level} | {module}:{function}:{line} | {message}"
    rotation: str = "2 MB"
    format_compression: str = "zip"
    default_dir: str = "logs"
    extension_files: str = "log"


class MainBotConfig(BaseSettings):
    """Main configuration storage class."""
    db: ConfigBD = Field(default_factory=ConfigBD)
    bot: BotConfig = Field(default_factory=BotConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)


config = MainBotConfig()
