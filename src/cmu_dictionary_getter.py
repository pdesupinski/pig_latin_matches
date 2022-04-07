from typing import Sequence

from src.dictionary_getter import DictionaryGetter
from src.util import remove_non_alpha
from src.word import Word


class CMUDictionaryGetter(DictionaryGetter):
    @staticmethod
    def get_words() -> Sequence[Word]:
        words = []
        with open("../cmudict.dict", "r") as f:
            for line in f:
                split = line.strip().split(" ")
                word = Word(
                    spelling=split[0],
                    pronunciation=tuple(
                        [remove_non_alpha(phone) for phone in split[1:]]
                    ),
                )
                words.append(word)
        return words
