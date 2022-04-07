from typing import Set, Mapping

from src.dictionary_getter import DictionaryGetter
from src.translator import Translator
from src.util import remove_non_alpha
from src.word import Word


class TranslationMatcher:
    def __init__(
        self, translator: Translator, dictionary_getter: DictionaryGetter
    ) -> None:
        self._translator: Translator = translator
        self._dictionary_getter: DictionaryGetter = dictionary_getter

    def get_word_to_translated_matches(self) -> Mapping[str, Set[str]]:
        words = self._dictionary_getter.get_words()
        pronunciations = {word.pronunciation for word in words}
        pronunciation_to_words = {
            pronunciation: set() for pronunciation in pronunciations
        }
        for word in words:
            pronunciation_to_words[word.pronunciation].add(word)
        word_to_translated_pronunciation = {
            word: self._translator.translate(word.pronunciation) for word in words
        }
        word_to_translated_matches = {
            word: pronunciation_to_words[translated_pronunciation]
            for word, translated_pronunciation in word_to_translated_pronunciation.items()
            if translated_pronunciation in pronunciation_to_words
        }
        return {
            word.spelling: {
                remove_non_alpha(translated_match.spelling)
                for translated_match in translated_matches
            }
            for word, translated_matches in word_to_translated_matches.items()
        }
