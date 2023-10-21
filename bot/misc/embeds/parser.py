import json
from enum import StrEnum, unique
from pathlib import Path

from discord.embeds import Embed


@unique
class EmbedJSONTypes(StrEnum):
    """JSON Embed files."""

    HELP = "help"

    @property
    def path(self) -> Path:
        """Returns the path to the json file with the desired embed."""
        return Path(__file__).parent / Path("source") / Path(f"{self.value}.json")


def get_embed_from_json(filename: EmbedJSONTypes) -> Embed:
    """Parse an embed from a file.

    Args:
        filename: The name (from enum) of the file to parse.

    Returns:
        Embed: The parsed embed object.
    """
    with open(filename.path, encoding="utf-8") as f:
        return Embed.from_dict(json.load(f))
