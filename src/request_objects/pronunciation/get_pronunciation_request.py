import dataclasses

from src.exception.errors import ValidationError


@dataclasses.dataclass
class GetPronunciationRequest:
    words: str

    def __post_init__(self):
        if not self.words:
            raise ValidationError("words is required.")
