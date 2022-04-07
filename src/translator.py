from abc import ABC, abstractmethod

from src.word import Pronunciation, Word


class Translator(ABC):
    @staticmethod
    @abstractmethod
    def translate(pronunciation: Pronunciation) -> Pronunciation:
        pass
