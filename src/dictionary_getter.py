from abc import ABC, abstractmethod
from typing import Sequence

from src.word import Word


class DictionaryGetter(ABC):
    @staticmethod
    @abstractmethod
    def get_words() -> Sequence[Word]:
        pass
