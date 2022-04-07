from src.cmu_dictionary_getter import CMUDictionaryGetter
from src.pig_latin_translator import PigLatinTranslator
from src.translation_matcher import TranslationMatcher

translation_matcher = TranslationMatcher(PigLatinTranslator(), CMUDictionaryGetter())
word_to_translated_matches = translation_matcher.get_word_to_translated_matches()
for word, translated_matches in word_to_translated_matches.items():
    print(f"{word}: {', '.join(translated_matches)}")
