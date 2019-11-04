import dataclasses
from typing import List

from src.entities.song import Song


@dataclasses.dataclass
class TitleSearchResponse:
    songs: List[Song]
