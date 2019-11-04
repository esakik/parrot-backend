import dataclasses


@dataclasses.dataclass(frozen=True)
class Song:
    artist: str
    title: str
    lyrics: str
    jacket_image_url: str
