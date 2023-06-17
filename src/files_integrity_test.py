# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:56:25 2020

@author: Alexander Mikhailov
"""

import os
import shutil
from pathlib import Path

# =============================================================================
# Script to Back-Up Empty Files from One Drive to Another
# =============================================================================
PATHS = (
    '/media/green-machine/KINGSTON',
    'E:',
)

os.chdir(PATHS[1])

empty_files_list = [
    file_name for file_name in os.listdir() if os.path.getsize(file_name) == 0
]
empty_files_list.remove('FOUND.000')
empty_files_list.remove('System Volume Information')

for file_name in empty_files_list:
    if Path(PATHS[0]).joinpath(file_name).exists():
        shutil.copy2(
            Path(PATHS[0]).joinpath(file_name),
            Path(PATHS[1]).joinpath(file_name)
        )
        print(f'Copied {file_name}')


files_list_d = {
    file_name.lower() for file_name in os.listdir(PATHS[0]) if not file_name.startswith(('.', '_', '~'))
}
files_list_e = {
    file_name.lower() for file_name in os.listdir(PATHS[1]) if not file_name.startswith(('.', '_', '~'))
}

for file_name in files_list_e - files_list_d:
    print(file_name)


def get_file_names(file_name: str) -> set[str]:
    with open(file_name, 'r') as source:
        return {
            _.rstrip().split('\\')[1] for _ in source.readlines()
            if not _.startswith(('.', '~'))
        }


def get_file_names(directory: str) -> set[str]:
    return {
        file_name.lower() for file_name in os.listdir(directory) if not file_name.startswith(('.', '_', '~'))
    }


file_names_d = get_file_names('list_d.txt')
file_names_e = get_file_names('list_e.txt')

file_names_d = get_file_names(PATHS[0])
file_names_d = get_file_names(PATHS[1])


set_difference = file_names_d - file_names_e

for file_name in set_difference:
    shutil.copy2(
        Path('/media/green-machine/KINGSTON').joinpath(file_name),
        Path('E:').joinpath(file_name)
    )
    print(f'Copied <{file_name}> from /media/green-machine/KINGSTON to E:')

set_difference = file_names_e - file_names_d

for file_name in set_difference:
    shutil.copy2(
        Path('E:').joinpath(file_name),
        Path('/media/green-machine/KINGSTON').joinpath(file_name)
    )
    print(f'Copied <{file_name}> from E: to /media/green-machine/KINGSTON')

for file_name in file_names_d - file_names_e:
    print(file_name)
