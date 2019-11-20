from abc import ABCMeta, abstractmethod

from src.request_objects.library.get_library_request import GetLibraryRequest
from src.response_objects.library.get_library_response import GetLibraryResponse


class AbstractGetLibraryUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: GetLibraryRequest) -> GetLibraryResponse:
        raise NotImplementedError()
