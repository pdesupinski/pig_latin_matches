from dataclasses import dataclass
from typing import Sequence, Type

Pronunciation: Type[object] = Sequence[str]


@dataclass(frozen=True)
class Word:
    spelling: str
    pronunciation: Pronunciation
