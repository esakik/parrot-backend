import dataclasses

from src.exception.error import ValidationError


@dataclasses.dataclass
class TitleSearchRequest:
    title: str

    def __post_init__(self):
        if not self.title:
            raise ValidationError("title is required.")
