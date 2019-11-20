import dataclasses

from src.exception.errors import ValidationError


@dataclasses.dataclass
class ArtistTitleSearchRequest:
    artist: str
    title: str

    def __post_init__(self):
        if not self.artist or not self.title:
            raise ValidationError("artist and title is required.")
