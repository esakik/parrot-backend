import dataclasses


@dataclasses.dataclass
class GetTrendingRequest:
    limit: int = 20
    offset: int = 0
