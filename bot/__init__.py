import logging

from loguru import logger

from bot.misc.config import LoggingConfig

logging.basicConfig(**LoggingConfig)

logger.add(
    "logs/debug.log",
    level="DEBUG",
    format="{time} | {level} | {module}:{function}:{line} | {message}",
    rotation="2 MB",
    compression="zip",
    filter=(lambda record: record["level"].name == "DEBUG"),
)

logger.add(
    "logs/error.log",
    level="ERROR",
    format="{time} | {level} | {module}:{function}:{line} | {message}",
    rotation="2 MB",
    compression="zip",
    backtrace=True,
    diagnose=True,
    filter=(lambda record: record["level"].name == "ERROR"),
)

logger.add(
    "logs/info.log",
    level="INFO",
    format="{time} | {level} | {module}:{function}:{line} | {message}",
    rotation="2 MB",
    compression="zip",
    filter=(lambda record: record["level"].name in ["INFO", "WARNING"]),
)
