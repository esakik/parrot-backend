import dataclasses

from src.exception.error import ValidationError


@dataclasses.dataclass
class CreateLibraryRequest:
    user_id: str

    def __post_init__(self):
        if not self.user_id:
            raise ValidationError("user id is required.")
