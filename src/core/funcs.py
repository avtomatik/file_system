#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 22:51:34 2023

@author: green-machine
"""

import json
import os
import re
import shutil
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
        shutil.copy2(
            path_src.joinpath(file_name),
            path_dst.joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {path_src} to {path_dst}')


def get_all_files_except(name_excluded: str, folder_str=None) -> tuple[str, ...]:
    path = Path(folder_str or '.')
    return tuple(
        file.name
        for file in path.iterdir()
        if file.is_file() and file.name != name_excluded
    )


def get_camel_to_snake_map(strings: tuple[str]) -> dict[str, str]:
    return dict(
        zip(
            strings,
            map(
                str.lower,
                map(
                    # =========================================================
                    # TODO: Figure Out How It Works
                    # =========================================================
                    lambda _: re.sub(r'(?<!^)(?=[A-Z])', '_', _),
                    strings
                )
            )
        )
    )


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


def get_names_walk(path):
    return map(lambda _: _[1:], os.walk(path))


def get_string_from_file(file_name: str) -> list[str]:
    with open(file_name) as f:
        return list(map(str.rstrip, f))


def get_set_from_text_file(file_path: Path) -> set[str]:
    return {
        line.rstrip().lower()
        for line in file_path.read_text(encoding='utf-8').splitlines()
    }


def move_files(file_names: tuple[str], path_src: Path, path_dst: Path) -> None:

    for file_name in file_names:
        shutil.move(
            path_src.joinpath(file_name),
            path_dst.joinpath(file_name)
        )
        print(f'Moved <{file_name}> from {path_src} to {path_dst}')


def rename_files(mapping: dict[str, str], path: Path) -> None:

    for src, dst in mapping.items():
        os.rename(
            path.joinpath(src),
            path.joinpath(dst)
        )

    print(f'{path}: Done')


def unlink_files(file_names: tuple[str], path: str) -> None:

    for file_name in file_names:
        path.joinpath(file_name).unlink()

    print(f'{path}: Done')


def transliterate(word: str, mapping: dict[str] = MAP_CYRILLIC_TO_LATIN) -> str:
    return ''.join(
        mapping[_.lower()] if _.lower() in mapping.keys() else _ for _ in word
    )


def trim_file_name(file_name: str) -> str:
    _file_name = f"{trim_string(Path(file_name).stem, '_')}{Path(file_name).suffix}"
    return transliterate('_'.join(filter(bool, _file_name.lower().split('_'))))


def trim_string(string: str, fill: str = ' ') -> str:
    return fill.join(filter(bool, re.split(r'\W', string)))


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
