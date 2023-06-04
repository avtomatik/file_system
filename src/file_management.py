#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 17:06:20 2022

@author: Alexander Mikhailov
"""

import os
import shutil
from pathlib import Path

from lib import copy_rename_files, get_set_from_text_file

if __name__ == '__main__':
    PATHS = ()
    MATCHERS = ('.csv',)
    PATH_SRC = '/home/green-machine/Downloads'

    FLAG = ''

    file_names = tuple(filter(lambda _: FLAG in _, os.listdir(PATH_SRC)))

    kwargs = {
        'dir_from': PATH_SRC,
        'dir_to': PATH_SRC,
        'file_names': file_names,
    }

    copy_rename_files(**kwargs)


def files_mirroring(file_names: tuple[str]) -> None:
    file_names_one = get_set_from_text_file(file_names[0])
    file_names_two = get_set_from_text_file(file_names[1])

    file_names_diff = file_names_one - file_names_two

    for file_name in file_names_diff:
        shutil.copy2(
            Path(PATHS[0]).joinpath(file_name),
            Path(PATHS[1]).joinpath(file_name)
        )
        print(f'Copied {file_name}')

    file_names_diff = file_names_two - file_names_one

    for file_name in file_names_diff:
        shutil.copy2(
            Path(PATHS[1]).joinpath(file_name),
            Path(PATHS[0]).joinpath(file_name)
        )
        print(f'Copied {file_name}')

