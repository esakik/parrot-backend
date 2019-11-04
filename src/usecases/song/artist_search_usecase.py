from abc import ABCMeta, abstractmethod

from src.usecases.song.requests.artist_search_request import ArtistSearchRequest
from src.usecases.song.responses.artist_search_response import ArtistSearchResponse


class ArtistSearchUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: ArtistSearchRequest) -> ArtistSearchResponse:
        raise NotImplementedError()
