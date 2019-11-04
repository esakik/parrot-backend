import dataclasses


@dataclasses.dataclass(frozen=True)
class Word:
    name: str
    phonetic_symbol: str
