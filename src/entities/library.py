import dataclasses
from typing import List

from src.entities.song import Song


@dataclasses.dataclass
class Library:
    user_id: str
    songs: List[Song]
