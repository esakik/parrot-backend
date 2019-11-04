from abc import ABCMeta, abstractmethod

from src.usecases.library.requests.get_library_request import GetLibraryRequest
from src.usecases.library.responses.get_library_response import GetLibraryResponse


class GetLibraryUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: GetLibraryRequest) -> GetLibraryResponse:
        raise NotImplementedError()
