from pydantic import BaseModel


class User(BaseModel):
    """User model.

    Attributes:
        id (int): User id
        messages_count (int): Messages count
        voice_time (int): Voice time in seconds
    """

    id: int
    messages_count: int
    voice_time: int
