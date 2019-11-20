from abc import ABCMeta, abstractmethod

from src.request_objects.library.create_library_request import CreateLibraryRequest
from src.response_objects.library.create_library_response import CreateLibraryResponse


class AbstractCreateLibraryUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: CreateLibraryRequest) -> CreateLibraryResponse:
        raise NotImplementedError()
