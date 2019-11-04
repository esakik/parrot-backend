from abc import ABCMeta, abstractmethod

from src.usecases.recommended.requests.get_recommended_request import GetRecommendedRequest
from src.usecases.recommended.responses.get_recommended_response import GetRecommendedResponse


class GetRecommendedUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: GetRecommendedRequest) -> GetRecommendedResponse:
        raise NotImplementedError()
