import logging

from loguru import logger

from bot.cogs.user.example import ExampleCommands
from bot.main import bot
from bot.utils.logs import InterceptHandler


def main() -> None:
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
    logger.level("CUSTOM", no=15, color="<yellow>", icon="🔥")
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
    logger.add(
        "logs/custom.log",
        level="CUSTOM",
        format="{time} | {level} | {module}:{function}:{line} | {message}",
        rotation="2 MB",
        compression="zip",
        filter=(lambda record: record["level"].name == "CUSTOM"),
    )

    bot.add_cog(ExampleCommands(bot))
    bot.run()


if __name__ == "__main__":
    main()
