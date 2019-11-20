from abc import ABCMeta, abstractmethod

from src.request_objects.song.artist_search_request import ArtistSearchRequest
from src.response_objects.song.artist_search_response import ArtistSearchResponse


class AbstractArtistSearchUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: ArtistSearchRequest) -> ArtistSearchResponse:
        raise NotImplementedError()
