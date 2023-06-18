#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 22:51:34 2023

@author: green-machine
"""

import io
import os
import shutil
from pathlib import Path

from core.constants import PREFIXES
from core.lib import get_file_names_set

# def get_set_from_text_file(file_name: str) -> set[str]:
#     with open(file_name, 'r') as f:
#         return {
#             _.rstrip().split('\\')[1] for _ in f.readlines()
#             if not _.startswith(PREFIXES)
#         }


def get_set_from_text_file(file_name: str) -> set:
    with io.open(file_name, mode='r', encoding='utf-8') as f:
        return set(map(str.lower, map(str.rstrip, f.readlines())))


def get_file_names_filter(prefixes: tuple[str], path: str = None) -> set[str]:
    return set(filter(lambda _: not _.startswith(prefixes), map(str.lower, os.listdir(path))))


PATH_SRC = '/media/green-machine/KINGSTON'
PATH_EXP = 'E:'

FILE_NAME_L = 'list_d.txt'
FILE_NAME_R = 'list_e.txt'


def files_mirroring(paths: tuple[str], file_names: tuple[str]) -> None:
    # =========================================================================
    # TODO: Review the Logic
    # =========================================================================
    file_names_l = get_set_from_text_file(file_names[0])
    file_names_r = get_set_from_text_file(file_names[1])

    for file_name in file_names_l - file_names_r:
        shutil.copy2(
            Path(paths[0]).joinpath(file_name),
            Path(paths[1]).joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {paths[0]} to {paths[1]}')

    for file_name in file_names_r - file_names_l:
        shutil.copy2(
            Path(paths[1]).joinpath(file_name),
            Path(paths[0]).joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {paths[1]} to {paths[0]}')


def files_mirroring(PATH_SRC, PATH_EXP):
    # =========================================================================
    # TODO: Review the Logic
    # =========================================================================
    file_names_l = get_file_names_set(PATH_SRC)
    file_names_r = get_file_names_set(PATH_EXP)

    file_names_diff = set(
        filter(
            lambda _: not _.startswith(PREFIXES),
            file_names_l - file_names_r
        )
    )

    for file_name in file_names_diff:
        shutil.copy2(
            Path(PATH_SRC).joinpath(file_name),
            Path(PATH_EXP).joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {PATH_SRC} to {PATH_EXP}')

    file_names_diff = set(
        filter(
            lambda _: not _.startswith(PREFIXES),
            file_names_r - file_names_l
        )
    )

    for file_name in file_names_diff:
        shutil.copy2(
            Path(PATH_EXP).joinpath(file_name),
            Path(PATH_SRC).joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {PATH_EXP} to {PATH_SRC}')


def files_mirroring(PATH_SRC, PATH_EXP, FILE_NAME_L, FILE_NAME_R):
    # =========================================================================
    # TODO: Review the Logic
    # =========================================================================
    file_names_l = get_set_from_text_file(FILE_NAME_L)
    file_names_r = get_set_from_text_file(FILE_NAME_R)

    file_names_l = get_file_names_filter(PREFIXES, PATH_SRC)
    file_names_r = get_file_names_filter(PREFIXES, PATH_EXP)

    for file_name in file_names_l - file_names_r:
        shutil.copy2(
            Path(PATH_SRC).joinpath(file_name),
            Path(PATH_EXP).joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {PATH_SRC} to {PATH_EXP}')

    for file_name in file_names_r - file_names_l:
        shutil.copy2(
            Path(PATH_EXP).joinpath(file_name),
            Path(PATH_SRC).joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {PATH_EXP} to {PATH_SRC}')
