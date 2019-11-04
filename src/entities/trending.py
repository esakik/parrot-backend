import dataclasses


@dataclasses.dataclass(frozen=True)
class Trending:
    title: str
    external_url: str
