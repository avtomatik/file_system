from pathlib import Path

from core.config import PATH
from mover.mover import FileMoverRenamer
from mover.protocols import FileTransformer
from tools.transformers import TrimFileNameTransformer
from utils.string import CyrillicToLatinTransliterator, RegexStringCleaner


class NullFileFilter:
    """A filter that accepts all regular files (ignores directories)."""

    def is_target(self, file: Path) -> bool:
        return file.is_file()


class FileExtensionFilter:
    def __init__(self, extensions: tuple[str, ...]):
        self.extensions = extensions

    def is_target(self, file: Path) -> bool:
        return file.is_file() and file.suffix in self.extensions


class TrimFileNameTransformerAdapter:
    """Adapter to make TrimFileNameTransformer compatible with FileTransformer protocol."""

    def __init__(self, transformer: TrimFileNameTransformer):
        self.transformer = transformer

    def transform(self, file_name: str) -> str:
        return self.transformer.transform(file_name)


class FileMoverAdapter:
    """Adapter to wrap FileMoverRenamer with the required transformer."""

    def __init__(self, transformer: FileTransformer):
        self.transformer = transformer

    def move_and_rename(
        self,
        src_dir: Path,
        dst_dir: Path,
        file_names: list[str]
    ) -> None:
        mover = FileMoverRenamer(self.transformer)
        mover.move_and_rename(src_dir, dst_dir, file_names)


def main():
    file_filter = NullFileFilter()  # Accept all files
    # Example usage:
    # file_filter = FileExtensionFilter(('.csv', '.txt'))
    cleaner = RegexStringCleaner(fill='_')
    transliterator = CyrillicToLatinTransliterator()
    transformer = TrimFileNameTransformer(cleaner, transliterator)
    mover = FileMoverAdapter(transformer)

    file_names = [
        f.name for f in PATH.iterdir()
        if file_filter.is_target(f)
    ]

    mover.move_and_rename(PATH, PATH, file_names)


if __name__ == '__main__':
    main()
