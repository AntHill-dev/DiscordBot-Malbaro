import logging
import sys

from loguru import logger


class InterceptHandler(logging.Handler):  # noqa: D101
    def emit(self, record):  # noqa: ANN001, D102, ANN201
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame = sys._getframe(6)  # noqa: SLF001
        depth = 6

        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())
