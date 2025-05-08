#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 22:51:34 2023

@author: green-machine
"""

import io
import os
import re
import shutil
from pathlib import Path

from core.constants import MAP_CYRILLIC_TO_LATIN

# def get_set_from_text_file(file_name: str) -> set[str]:
#     with open(file_name) as f:
#         return {
#             _.rstrip().split('\\')[1] for _ in f.readlines()
#             if not _.startswith(PREFIXES)
#         }


# def get_file_names_match(matchers: tuple[str], path: str = None) -> list[str]:
#     return [
#         file_name for file_name in tuple(os.listdir(path)) if any(match in file_name for match in matchers)
#     ]


def copy2_files(file_names: tuple[str], path_src: str, path_dst: str) -> None:

    for file_name in file_names:
        shutil.copy2(
            path_src.joinpath(file_name),
            path_dst.joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {path_src} to {path_dst}')


def get_all_files_except(string: str) -> tuple[str]:
    return tuple(filter(lambda _: _ != string, os.listdir()))


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


def get_file_names_filter(prefixes: tuple[str], path: str = None) -> set[str]:
    return set(filter(lambda _: not _.startswith(prefixes), map(str.lower, os.listdir(path))))


def get_file_names_match(matchers: tuple[str], path: str = None) -> list[str]:
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
    return [
        file_name for file_name in os.listdir(path) if all(match in file_name for match in matchers)
    ]


def get_file_names_set(path):
    return set(map(str.lower, os.listdir(path)))


def get_names_walk(path):
    return map(lambda _: _[1:], os.walk(path))


def get_string_from_file(file_name: str) -> list[str]:
    with open(file_name) as f:
        return list(map(str.rstrip, f))


def get_set_from_text_file(file_name: str) -> set:
    with io.open(file_name, encoding='utf-8') as f:
        return set(map(str.lower, map(str.rstrip, f.readlines())))


def move_files(file_names: tuple[str], path_src: str, path_dst: str) -> None:

    for file_name in file_names:
        shutil.move(
            path_src.joinpath(file_name),
            path_dst.joinpath(file_name)
        )
        print(f'Moved <{file_name}> from {path_src} to {path_dst}')


def rename_files(mapping: dict[str, str], path: str) -> None:

    for fn_in, fn_ut in mapping.items():
        os.rename(
            path.joinpath(fn_in),
            path.joinpath(fn_ut)
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


def copy_rename_files(path_src: str, path_dst: str, file_names: tuple[str]) -> None:
    """
    Copies <shutil.copy2> or Moves <shutil.move> Files
    Parameters
    ----------
    path_from : str
        Source Directory.
    path_to : str
        Destination Directory.
    file_names : tuple[str]
        File Names Set.
    Returns
    -------
    None
    """
    os.chdir(path_src)
    LOG = []
    for file_name in file_names:
        if path_src.joinpath(file_name).exists():
            shutil.move(
                path_src.joinpath(file_name),
                path_dst.joinpath(trim_file_name(file_name))
            )

            # =====================================================================
            # Logging
            # =====================================================================
            LOG.append(
                {
                    'from': file_name,
                    'to': trim_file_name(file_name),
                }
            )

    # filepath = Path(PATH_LOG).joinpath(FILE_NAME_LOG)
    # with open(filepath, 'w') as f:
    #     json.dump(LOG, f, ensure_ascii=False)

    print(f'Moved {len(LOG)} Files')
