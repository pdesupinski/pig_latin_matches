from src.translator import Translator
from src.util import is_vowel
from src.word import Pronunciation, Word


class PigLatinTranslator(Translator):
    @staticmethod
    def translate(pronunciation: Pronunciation) -> Pronunciation:
        translated_pronunciation = []
        beginning_consonant_phones = []
        has_encountered_vowel = False
        for phone in pronunciation:
            has_encountered_vowel = has_encountered_vowel or is_vowel(phone[0])
            if has_encountered_vowel:
                translated_pronunciation.append(phone)
            else:
                beginning_consonant_phones.append(phone)
        translated_pronunciation = (
            translated_pronunciation + beginning_consonant_phones + ["EY"]
        )
        return tuple(translated_pronunciation)
