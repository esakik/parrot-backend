from abc import ABCMeta, abstractmethod

from src.request_objects.song.artist_title_search_request import ArtistTitleSearchRequest
from src.response_objects.song.artist_title_search_response import ArtistTitleSearchResponse


class AbstractArtistTitleSearchUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: ArtistTitleSearchRequest) -> ArtistTitleSearchResponse:
        raise NotImplementedError()
