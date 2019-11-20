import dataclasses


@dataclasses.dataclass
class GetRecommendedRequest:
    limit: int = 10
    offset: int = 0
