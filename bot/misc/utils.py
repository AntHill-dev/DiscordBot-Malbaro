from abc import ABCMeta
from typing import Any, ClassVar

from discord import Intents

from bot.misc.types import IntentsType


def get_default_msg_intents() -> IntentsType:
    intents = Intents.default()
    # noinspection PyDunderSlots,PyUnresolvedReferences
    intents.message_content = True
    return intents


class SingletonABC(ABCMeta):
    _instances: ClassVar[dict] = {}

    def __call__(cls: Any, *args: Any, **kwargs: Any):  # type: ignore  # noqa: ANN204
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
