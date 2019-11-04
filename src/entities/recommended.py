import dataclasses


@dataclasses.dataclass(frozen=True)
class Recommended:
    artist: str
    title: str
    jacket_image_url: str
    external_url: str
