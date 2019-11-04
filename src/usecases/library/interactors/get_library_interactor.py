import logging

from src.adapters.gateways.library_gateway import LibraryGateway
from src.exception.error import UnexpectedError
from src.usecases.library.get_library_usecase import GetLibraryUseCase
from src.usecases.library.requests.get_library_request import GetLibraryRequest
from src.usecases.library.responses.get_library_response import GetLibraryResponse


class GetLibraryInteractor(GetLibraryUseCase):
    def __init__(self, library_gateway: LibraryGateway):
        self._library_gateway = library_gateway

    def handle(self, request: GetLibraryRequest) -> GetLibraryResponse:
        try:
            library = self._library_gateway.find_by_user_id(request.user_id)
        except Exception as e:
            logging.exception(e)
            raise UnexpectedError("Failed to get library.")

        return GetLibraryResponse(library)
