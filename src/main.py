#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 17:06:20 2022

@author: Alexander Mikhailov
"""

import os

from core.config import PATH
from core.funcs import copy_rename_files

if __name__ == '__main__':

    MATCHERS = ['.csv']

    FLAG = ''

    file_names = tuple(filter(lambda _: FLAG in _, os.listdir(PATH)))

    kwargs = {
        'path_from': PATH,
        'path_to': PATH,
        'file_names': file_names,
    }

    copy_rename_files(**kwargs)
