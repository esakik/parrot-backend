from abc import ABCMeta, abstractmethod

from src.request_objects.song.title_search_request import TitleSearchRequest
from src.response_objects.song.title_search_response import TitleSearchResponse


class AbstractTitleSearchUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: TitleSearchRequest) -> TitleSearchResponse:
        raise NotImplementedError()
