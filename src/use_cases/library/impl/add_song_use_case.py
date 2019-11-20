import logging

from src.adapters.repositories.library_repository import LibraryRepository
from src.entities.library import Library
from src.entities.song import Song
from src.exception.errors import UnexpectedError
from src.request_objects.library.add_song_request import AddSongRequest
from src.response_objects.library.add_song_response import AddSongResponse
from src.use_cases.library.add_song_use_case import AbstractAddSongUseCase


class AddSongUseCase(AbstractAddSongUseCase):
    def __init__(self, library_repo: LibraryRepository):
        self._library_repo = library_repo

    def handle(self, request: AddSongRequest) -> AddSongResponse:
        try:
            user_id = self._library_repo.update(
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
