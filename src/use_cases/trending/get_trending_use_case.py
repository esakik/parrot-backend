from abc import ABCMeta, abstractmethod

from src.request_objects.trending.get_trending_request import GetTrendingRequest
from src.response_objects.trending.get_trending_response import GetTrendingResponse


class AbstractGetTrendingUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: GetTrendingRequest) -> GetTrendingResponse:
        raise NotImplementedError()
