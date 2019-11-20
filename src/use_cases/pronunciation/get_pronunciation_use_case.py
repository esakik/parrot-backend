from abc import ABCMeta, abstractmethod

from src.request_objects.pronunciation.get_pronunciation_request import GetPronunciationRequest
from src.response_objects.pronunciation.get_pronunciation_response import GetPronunciationResponse


class AbstractGetPronunciationUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: GetPronunciationRequest) -> GetPronunciationResponse:
        raise NotImplementedError()
