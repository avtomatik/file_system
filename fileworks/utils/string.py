import re
from typing import Protocol

from core.constants import CYRILLIC_TO_LATIN

# ==========================
# Protocols (Interfaces)
# ==========================


class StringCleaner(Protocol):
    def clean(self, string: str) -> str:
        ...


class Transliterator(Protocol):
    def transliterate(self, text: str) -> str:
        ...


# ==========================
# Concrete Implementations
# ==========================

class RegexStringCleaner:
    def __init__(self, fill: str = ' '):
        self.fill = fill

    def clean(self, string: str) -> str:
        split_string = re.split(r'\W', string)
        return self.fill.join(part for part in split_string if part)


class CyrillicToLatinTransliterator:
    def __init__(self, mapping: dict[str, str] = CYRILLIC_TO_LATIN):
        self.mapping = mapping

    def transliterate(self, text: str) -> str:
        return ''.join(self.mapping.get(char, char) for char in text.lower())
