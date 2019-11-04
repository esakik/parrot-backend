from abc import ABCMeta, abstractmethod
from typing import List

from src.entities.word import Word


class WordGateway(metaclass=ABCMeta):
    @abstractmethod
    def find_by_names(self, names: List[str]) -> List[Word]:
        raise NotImplementedError()
