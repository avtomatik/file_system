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

from core.config import PATH_LOG
from core.constants import FILE_NAME_LOG, MAP_CYRILLIC_TO_LATIN, PREFIXES


def get_set_from_text_file(file_path: Path, prefixes=PREFIXES) -> set[str]:
    return {
        line.split('\\')[1]
        for line in file_path.read_text().splitlines()
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
    result = {}
    for string in strings:
        # Convert CamelCase to snake_case
        snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
        result[string] = snake_case
    return result


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


def get_set_from_text_file(file_path: Path) -> set[str]:
    return {
        line.rstrip().lower()
        for line in file_path.read_text(encoding='utf-8').splitlines()
    }


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
    word_lower = word.lower()

    result = []

    for char in word_lower:
        if char in mapping:
            result.append(mapping[char])
        else:
            result.append(char)

    return ''.join(result)


def trim_file_name(file_path: Path) -> str:
    file_stem = file_path.stem

    trimmed_name = trim_string(file_stem, '_')

    file_suffix = file_path.suffix

    transliterated_name = transliterate(trimmed_name)

    return f'{transliterated_name}{file_suffix}'


def trim_string(string: str, fill: str = ' ') -> str:
    split_string = re.split(r'\W', string)

    cleaned_string = []

    for part in split_string:
        if not part:
            continue
        cleaned_string.append(part)

    return fill.join(cleaned_string)


def move_and_rename_files(
    path_src: Path,
    path_dst: Path,
    file_names: tuple[str]
) -> None:
    """
    Moves files from one to another folder with renamed filenames.

    Parameters
    ----------
    path_src : Path
        Source Directory Path.
    path_dst : Path
        Destination Directory Path.
    file_names : tuple[str]
        File Names to Move and Rename.

    Returns
    -------
    None
        Nothing.

    """

    logs = []

    for file_name in file_names:
        name_src = path_src.joinpath(file_name)

        if not name_src.exists():
            continue

        name_new = trim_file_name(file_name)
        name_dst = path_dst.joinpath(name_new)

        name_dst.parent.mkdir(parents=True, exist_ok=True)
        name_src.rename(name_dst)

        # =====================================================================
        # Logging
        # =====================================================================
        if file_name != name_new:
            logs.append({'src': file_name, 'dst': name_new})

    if logs:
        logs_path = PATH_LOG.joinpath(FILE_NAME_LOG)
        with logs_path.open('w', encoding='utf-8') as f:
            json.dump(logs, f, ensure_ascii=False, indent=4)

        print(f'Renamed and Moved {len(logs)} Files')
    else:
        print('No Files Were Renamed')
