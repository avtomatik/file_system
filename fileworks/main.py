from pathlib import Path

from core.config import PATH
from mover.mover import FileMoverRenamer
from mover.protocols import FileTransformer
from tools.transformers import TrimFileNameTransformer


class CsvFileFilter:
    def is_target(self, file: Path) -> bool:
        return file.suffix == '.csv'


class TrimFileNameTransformerAdapter:
    def __init__(self, transformer: TrimFileNameTransformer):
        self.transformer = transformer

    def transform(self, file_name: str) -> str:
        return self.transformer.transform(file_name)


class FileMoverAdapter:
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


MATCHERS = ('.csv',)


def main():
# =============================================================================
# TODO: Take Extension as Argument
# =============================================================================
    file_filter = CsvFileFilter()
    transformer = TrimFileNameTransformerAdapter(TrimFileNameTransformer())
    mover = FileMoverAdapter(transformer)

    file_names = [
        f.name for f in PATH.iterdir()
        if file_filter.is_target(f)
    ]

    mover.move_and_rename(PATH, PATH, file_names)


if __name__ == '__main__':
    main()
