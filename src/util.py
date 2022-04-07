from typing import Set

VOWELS: Set[str] = {"a", "e", "i", "o", "u"}


def is_vowel(char: str) -> bool:
    return char.lower() in VOWELS


def remove_non_alpha(s: str) -> str:
    result = ""
    for char in s:
        if char.isalpha():
            result += char
    return result
