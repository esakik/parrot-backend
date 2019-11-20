import logging

from src.adapters.repositories.library_repository import LibraryRepository
from src.exception.errors import UnexpectedError
from src.request_objects.library.create_library_request import CreateLibraryRequest
from src.response_objects.library.create_library_response import CreateLibraryResponse
from src.use_cases.library.create_library_use_case import AbstractCreateLibraryUseCase


class CreateLibraryUseCase(AbstractCreateLibraryUseCase):
    def __init__(self, library_repo: LibraryRepository):
        self._library_repo = library_repo

    def handle(self, request: CreateLibraryRequest) -> CreateLibraryResponse:
        try:
            user_id = self._library_repo.insert(request.user_id)
        except Exception as e:
            logging.exception(e)
            raise UnexpectedError("Failed to create library.")

        return CreateLibraryResponse(user_id)
