import logging
import sys

from loguru import logger


class InterceptHandler(logging.Handler):  # noqa: D101
    def emit(self, record):
        # Получаем соответствующий уровень `Loguru`, если он существует..
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Ищем вызывающего абонента, откуда поступило зарегистрированное сообщение.
        frame, depth = sys._getframe(6), 6
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())
