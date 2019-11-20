import dataclasses

from src.exception.errors import ValidationError


@dataclasses.dataclass
class GetLibraryRequest:
    user_id: str

    def __post_init__(self):
        if not self.user_id:
            raise ValidationError("user id is required.")
