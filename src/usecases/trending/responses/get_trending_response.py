import dataclasses
from typing import List

from src.entities.trending import Trending


@dataclasses.dataclass
class GetTrendingResponse:
    trending: List[Trending]
