import dataclasses
from typing import List

from src.entities.recommended import Recommended


@dataclasses.dataclass
class GetRecommendedResponse:
    recommended: List[Recommended]
