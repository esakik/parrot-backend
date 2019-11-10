import logging

from src.adapters.repositories.library_repository import LibraryRepository
from src.exception.error import UnexpectedError
from src.usecases.library.create_library_usecase import CreateLibraryUseCase
from src.usecases.library.requests.create_library_request import CreateLibraryRequest
from src.usecases.library.responses.create_library_response import CreateLibraryResponse


class CreateLibraryInteractor(CreateLibraryUseCase):
    def __init__(self, library_repo: LibraryRepository):
        self._library_repo = library_repo

    def handle(self, request: CreateLibraryRequest) -> CreateLibraryResponse:
        try:
            user_id = self._library_repo.insert(request.user_id)
        except Exception as e:
            logging.exception(e)
            raise UnexpectedError("Failed to create library.")

        return CreateLibraryResponse(user_id)
