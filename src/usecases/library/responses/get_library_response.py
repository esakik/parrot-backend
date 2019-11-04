import dataclasses

from src.entities.library import Library


@dataclasses.dataclass
class GetLibraryResponse:
    library: Library
