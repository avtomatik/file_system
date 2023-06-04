# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:56:25 2020

@author: Alexander Mikhailov
"""

import shutil
from pathlib import Path

from lib import get_file_names_set

PATHS = (
    'D:',
    'E:',
)


def main():
    # TODO: Review the Logic
    file_names_d = get_file_names_set(PATHS[0])
    file_names_e = get_file_names_set(PATHS[1])

    file_names_difference = file_names_d - file_names_e
    file_names = {
        _ for _ in file_names_difference if not _.startswith(('.', '~'))
    }

    for file_name in file_names:
        shutil.copy2(
            Path(PATHS[0]).joinpath(file_name),
            Path(PATHS[1]).joinpath(file_name)
        )
        print(f'Copied {file_name}')

    file_names_difference = file_names_e - file_names_d
    file_names = {
        _ for _ in file_names_difference if not _.startswith(('.', '~'))
    }

    for file_name in file_names:
        shutil.copy2(
            Path(PATHS[1]).joinpath(file_name),
            Path(PATHS[0]).joinpath(file_name)
        )
        print(f'Copied {file_name}')


if __name__ == '__main__':
    main()
