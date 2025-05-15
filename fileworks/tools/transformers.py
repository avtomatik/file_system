from pathlib import Path

from utils.string import clean_string, transliterate_to_latin


def generate_trimmed_file_name(file_path: Path) -> str:
    file_stem = file_path.stem
    trimmed_name = clean_string(file_stem, '_')
    file_suffix = file_path.suffix
    return f'{transliterate_to_latin(trimmed_name)}{file_suffix}'


class TrimFileNameTransformer:
    def transform(self, file_name: str) -> str:
        return generate_trimmed_file_name(Path(file_name))
