from abc import ABCMeta
from collections.abc import Sequence
from typing import Any, ClassVar

from discord import Intents

from bot.misc.logs import InterceptHandler
from bot.misc.types import HandlerType, IntentsType


def get_default_intents() -> IntentsType:
    """Returns default intents with certain presets.

    Specific settings: enabled message contents.

    Returns:
        Standard intents, but with message content included.
    """
    intents = Intents.default()
    # noinspection PyDunderSlots,PyUnresolvedReferences
    intents.message_content = True
    intents.members = True
    return intents


def get_handlers_for_filtered() -> Sequence[HandlerType]:
    """Function for generating a sequence of handlers for logging."""
    handlers_obj = (InterceptHandler,)
    return [handler() for handler in handlers_obj]


class SingletonABC(ABCMeta):
    """Singleton pattern metaclass."""

    _instances: ClassVar[dict] = {}

    def __call__(cls: Any, *args: Any, **kwargs: Any):  # type: ignore  # noqa: ANN204 D102
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
