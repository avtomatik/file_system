#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:56:25 2020

@author: Alexander Mikhailov
"""

import os
import shutil

from core.config import PATH_DST, PATH_SRC

# =============================================================================
# Script to Back-Up Empty Files from One Drive to Another
# =============================================================================

empty_files_list = [
    file_name for file_name in os.listdir(PATH_DST) if os.path.getsize(file_name) == 0
]
empty_files_list.remove('FOUND.000')
empty_files_list.remove('System Volume Information')

for file_name in empty_files_list:
    if PATH_SRC.joinpath(file_name).exists():
        shutil.copy2(
            PATH_SRC.joinpath(file_name),
            PATH_DST.joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {PATH_SRC} to {PATH_DST}')
