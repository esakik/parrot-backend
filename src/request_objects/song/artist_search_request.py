import dataclasses

from src.exception.errors import ValidationError


@dataclasses.dataclass
class ArtistSearchRequest:
    artist: str

    def __post_init__(self):
        if not self.artist:
            raise ValidationError("artist is required.")
