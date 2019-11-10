import dataclasses

from src.exception.error import ValidationError


@dataclasses.dataclass
class AddSongRequest:
    user_id: str
    artist: str
    title: str
    lyrics: str
    jacket_image_url: str

    # TODO Cerberusでバリデーション
    def __post_init__(self):
        if not self.user_id:
            raise ValidationError("user id is required.")
        elif not self.artist:
            raise ValidationError("artist is required.")
        elif not self.title:
            raise ValidationError("title is required.")
        elif not self.lyrics:
            raise ValidationError("lyrics is required.")
        elif not self.jacket_image_url:
            raise ValidationError("jacket image url is required.")
