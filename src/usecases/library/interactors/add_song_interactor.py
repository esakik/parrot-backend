import logging

from src.adapters.gateways.library_gateway import LibraryGateway
from src.entities.library import Library
from src.entities.song import Song
from src.exception.error import UnexpectedError
from src.usecases.library.add_song_usecase import AddSongUseCase
from src.usecases.library.requests.add_song_request import AddSongRequest
from src.usecases.library.responses.add_song_response import AddSongResponse


class AddSongInteractor(AddSongUseCase):
    def __init__(self, library_gateway: LibraryGateway):
        self._library_gateway = library_gateway

    def handle(self, request: AddSongRequest) -> AddSongResponse:
        try:
            user_id = self._library_gateway.update(
                Library(
                    user_id=request.user_id,
                    songs=[
                        Song(
                            artist=request.artist,
                            title=request.title,
                            lyrics=request.lyrics,
                            jacket_image_url=request.jacket_image_url,
                        )
                    ],
                )
            )
        except Exception as e:
            logging.exception(e)
            raise UnexpectedError("Failed to create library.")

        return AddSongResponse(user_id)
