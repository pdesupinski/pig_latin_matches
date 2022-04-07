from typing import Sequence

from src.word import Word

def get_words_from_dataset() -> Sequence[Word]:
    words = []
    with open("../cmudict.dict", "r") as f:
        for line in f:
            split = line.strip().split(" ")
            word = Word(spelling=split[0], pronunciation=" ".join(split[1:]))
            words.append(word)
    return words

