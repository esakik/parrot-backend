import dataclasses

from src.exception.error import ValidationError


@dataclasses.dataclass
class ArtistSearchRequest:
    artist: str

    def __post_init__(self):
        if not self.artist:
            raise ValidationError("artist is required.")
