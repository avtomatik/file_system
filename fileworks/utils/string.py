import re

from fileworks.core.constants import MAP_CYRILLIC_TO_LATIN


def clean_string(string: str, fill: str = ' ') -> str:
    split_string = re.split(r'\W', string)
    return fill.join(part for part in split_string if part)


def transliterate_to_latin(
    word: str,
    mapping: dict[str, str] = MAP_CYRILLIC_TO_LATIN
) -> str:
    return ''.join(mapping.get(char, char) for char in word.lower())
