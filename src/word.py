from dataclasses import dataclass
from typing import Tuple, Type

Pronunciation: Type[object] = Tuple[str, ...]


@dataclass(frozen=True)
class Word:
    spelling: str
    pronunciation: Pronunciation
