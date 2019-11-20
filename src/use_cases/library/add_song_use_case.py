from abc import ABCMeta, abstractmethod

from src.request_objects.library.add_song_request import AddSongRequest
from src.response_objects.library.add_song_response import AddSongResponse


class AbstractAddSongUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: AddSongRequest) -> AddSongResponse:
        raise NotImplementedError()
