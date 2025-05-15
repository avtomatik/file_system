from pathlib import Path
from typing import Protocol


class FileNameTransformer(Protocol):
    def transform(self, file_name: str) -> str:
        ...


class Logger(Protocol):
    def log(self, entries: list[dict]) -> None:
        ...


class FileFilter(Protocol):
    def is_target(self, file: Path) -> bool:
        ...


class FileTransformer(Protocol):
    def transform(self, file_name: str) -> str:
        ...


class FileMover(Protocol):
    def move_and_rename(self, src_dir: Path, dst_dir: Path, file_names: list[str]) -> None:
        ...
