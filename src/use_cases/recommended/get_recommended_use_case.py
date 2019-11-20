from abc import ABCMeta, abstractmethod

from src.request_objects.recommended.get_recommended_request import GetRecommendedRequest
from src.response_objects.recommended.get_recommended_response import GetRecommendedResponse


class AbstractGetRecommendedUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: GetRecommendedRequest) -> GetRecommendedResponse:
        raise NotImplementedError()
