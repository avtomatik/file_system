import argparse
from pathlib import Path

from fileworks.interfaces.protocols import FileTransformer
from fileworks.tools.cleaners import (CyrillicToLatinTransliterator,
                                      RegexStringCleaner)
from fileworks.tools.filters import FileExtensionFilter, NullFileFilter
from fileworks.tools.movers import FileMoverRenamer
from fileworks.tools.transformers import TrimFileNameTransformer


class TrimFileNameTransformerAdapter:
    """Adapter to make TrimFileNameTransformer compatible with FileTransformer
    protocol."""

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
    parser = argparse.ArgumentParser(description='FileWorks CLI')
    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='Path to the directory to process (default: current directory)'
    )
    parser.add_argument(
        '-e', '--extensions',
        nargs='+',
        help='Filter files by extensions (space separated, e.g. -e csv txt)'
    )
    args = parser.parse_args()

    PATH = Path(args.path).resolve()

    if args.extensions:
        file_filter = FileExtensionFilter(tuple(args.extensions))
    else:
        file_filter = NullFileFilter()

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
