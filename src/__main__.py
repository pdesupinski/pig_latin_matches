from src.cmu_dictionary_getter import CMUDictionaryGetter
from src.pig_latin_translator import PigLatinTranslator
from src.translation_matcher import TranslationMatcher

translation_matcher = TranslationMatcher(PigLatinTranslator(), CMUDictionaryGetter())
print(str(translation_matcher.get_all_matches()))
