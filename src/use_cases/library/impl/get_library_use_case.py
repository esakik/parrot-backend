import logging

from src.adapters.repositories.library_repository import LibraryRepository
from src.exception.errors import UnexpectedError
from src.request_objects.library.get_library_request import GetLibraryRequest
from src.response_objects.library.get_library_response import GetLibraryResponse
from src.use_cases.library.get_library_use_case import AbstractGetLibraryUseCase


class GetLibraryUseCase(AbstractGetLibraryUseCase):
    def __init__(self, library_repo: LibraryRepository):
        self._library_repo = library_repo

    def handle(self, request: GetLibraryRequest) -> GetLibraryResponse:
        try:
            library = self._library_repo.find_by_user_id(request.user_id)
        except Exception as e:
            logging.exception(e)
            raise UnexpectedError("Failed to get library.")

        return GetLibraryResponse(library)
