#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 22:51:34 2023

@author: green-machine
"""

import json
import os
import re
from pathlib import Path
from typing import Iterable, Optional, Protocol

from core.config import PATH_LOG
from core.constants import FILE_NAME_LOG, MAP_CYRILLIC_TO_LATIN, PREFIXES


def get_set_from_text_file(file_path: Path, prefixes=PREFIXES) -> set[str]:
    return {
        Path(line).name
        for line in file_path.read_text(encoding='utf-8').splitlines()
        if line and not any(line.startswith(prefix) for prefix in prefixes)
    }


def copy2_files(file_names: tuple[str], path_src: Path, path_dst: Path) -> None:
    for file_name in file_names:
        file_path_src = path_src / file_name
        file_path_dst = path_dst / file_name

        file_path_dst.parent.mkdir(parents=True, exist_ok=True)
        with file_path_src.open('rb') as fsrc, file_path_dst.open('wb') as fdst:
            fdst.write(fsrc.read())

        print(f'Copied <{file_name}> from {path_src} to {path_dst}')


def get_all_files_except(name_excluded: str, folder_str=None) -> tuple[str, ...]:
    path = Path(folder_str or '.')
    return tuple(
        file.name
        for file in path.iterdir()
        if file.is_file() and file.name != name_excluded
    )


def generate_snake_case_map(strings: tuple[str]) -> dict[str, str]:
    return {
        string: re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
        for string in strings
    }


def get_file_names_filter(prefixes: set[str] = PREFIXES, folder_str=None) -> set[str]:
    path = Path(folder_str or '.')
    return {
        file.name.lower()
        for file in path.iterdir()
        if file.is_file() and not any(
            file.name.lower().startswith(prefix) for prefix in prefixes
        )
    }


def get_file_names_match(matchers: tuple[str], folder_str=None) -> list[str]:
    """
    Comprehension Filter for Files in Folder
    Parameters
    ----------
        matchers : tuple[str]
    Returns
    -------
        list[str]
    """
    # =========================================================================
    # TODO: any OR all
    # =========================================================================
    path = Path(folder_str or '.')
    return [
        file.name
        for file in path.iterdir()
        if file.is_file() and all(matcher in file.name for matcher in matchers)
    ]


# def get_file_names_match(matchers: tuple[str], folder_str=None) -> list[str]:
#     path = Path(folder_str or '.')
#     return [
#         file.name
#         for file in path.iterdir()
#         if file.is_file() and any(matcher in file.name for matcher in matchers)
#     ]


def get_file_names_set(path: Path) -> set[str]:
    return {f.name.lower() for f in Path(path).iterdir() if f.is_file()}


def get_names_walk(folder_str: str):
    result = []
    for _, dirnames, filenames in os.walk(folder_str):
        result.append((dirnames, filenames))
    return result


def get_string_from_file(file_path: Path) -> list[str]:
    return [line.rstrip() for line in file_path.read_text().splitlines()]


def move_files(file_names: tuple[str], path_src: Path, path_dst: Path) -> None:
    path_dst.mkdir(parents=True, exist_ok=True)

    for file_name in file_names:
        src = path_src / file_name
        dst = path_dst / file_name

        src.rename(dst)
        print(f'Moved <{file_name}> from {path_src} to {path_dst}')


def rename_files(mapping: dict[str, str], path: Path) -> None:
    for src, dst in mapping.items():
        src_path = path / src
        dst_path = path / dst
        src_path.rename(dst_path)

    print(f'{path}: Done')


def unlink_files(file_names: tuple[str], path: Path) -> None:

    for file_name in file_names:
        path.joinpath(file_name).unlink()

    print(f'{path}: Done')


def transliterate(word: str, mapping: dict[str] = MAP_CYRILLIC_TO_LATIN) -> str:
    return ''.join(mapping.get(char, char) for char in word.lower())


def trim_file_name(file_path: Path) -> str:
    file_stem = file_path.stem
    trimmed_name = trim_string(file_stem, '_')
    file_suffix = file_path.suffix
    return f'{transliterate(trimmed_name)}{file_suffix}'


def trim_string(string: str, fill: str = ' ') -> str:
    split_string = re.split(r'\W', string)
    return fill.join(part for part in split_string if part)


class FileNameTransformer(Protocol):
    def transform(self, file_name: str) -> str:
        ...


class Logger(Protocol):
    def log(self, entries: list[dict]) -> None:
        ...


class NullLogger:
    def log(self, entries: list[dict]) -> None:
        ...


class TrimFileNameTransformer:
    def transform(self, file_name: str) -> str:
        return trim_file_name(file_name)


class JsonFileLogger:
    def __init__(self, log_path: Path):
        self.log_path = log_path

    def log(self, entries: list[dict]) -> None:
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        with self.log_path.open('w', encoding='utf-8') as f:
            json.dump(entries, f, ensure_ascii=False, indent=4)
        print(f'Renamed and Moved {len(entries)} Files')


class FileMoverRenamer:
    def __init__(
        self,
        transformer: FileNameTransformer,
        logger: Optional[Logger] = None
    ):
        self.transformer = transformer
        self.logger = logger or NullLogger()  # Fallback to NullLogger

    def move_and_rename(
        self,
        src_dir: Path,
        dst_dir: Path,
        file_names: Iterable[str]
    ) -> None:
        logs = []

        for file_name in file_names:
            src_path = src_dir / file_name
            if not src_path.exists():
                continue

            new_name = self.transformer.transform(file_name)
            dst_path = dst_dir / new_name
            dst_path.parent.mkdir(parents=True, exist_ok=True)

            src_path.rename(dst_path)

            if file_name != new_name:
                logs.append({'src': file_name, 'dst': new_name})

        if logs:
            self.logger.log(logs)
        else:
            print('No Files Were Renamed')
