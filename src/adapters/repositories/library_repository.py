from abc import ABCMeta, abstractmethod

from src.entities.library import Library


class LibraryRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_by_user_id(self, user_id: str) -> Library:
        raise NotImplementedError()

    @abstractmethod
    def insert(self, user_id: str) -> str:
        raise NotImplementedError()

    @abstractmethod
    def update(self, library: Library) -> str:
        raise NotImplementedError()
