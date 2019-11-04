from abc import ABCMeta, abstractmethod

from src.usecases.song.requests.title_search_request import TitleSearchRequest
from src.usecases.song.responses.title_search_response import TitleSearchResponse


class TitleSearchUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: TitleSearchRequest) -> TitleSearchResponse:
        raise NotImplementedError()
