import dataclasses
from typing import List


@dataclasses.dataclass
class GetPronunciationResponse:
    pronunciation: List[str]
