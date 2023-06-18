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
PATH_SRC = '/media/green-machine/KINGSTON'
PATH_EXP = 'E:'

os.chdir(PATH_EXP)

empty_files_list = [
    file_name for file_name in os.listdir() if os.path.getsize(file_name) == 0
]
empty_files_list.remove('FOUND.000')
empty_files_list.remove('System Volume Information')

for file_name in empty_files_list:
    if Path(PATH_SRC).joinpath(file_name).exists():
        shutil.copy2(
            Path(PATH_SRC).joinpath(file_name),
            Path(PATH_EXP).joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {PATH_SRC} to {PATH_EXP}')
