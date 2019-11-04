from abc import ABCMeta, abstractmethod

from src.usecases.library.requests.add_song_request import AddSongRequest
from src.usecases.library.responses.add_song_response import AddSongResponse


class AddSongUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: AddSongRequest) -> AddSongResponse:
        raise NotImplementedError()
