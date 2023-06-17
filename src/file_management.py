#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 17:06:20 2022

@author: Alexander Mikhailov
"""

import os

from core.lib import copy_rename_files

if __name__ == '__main__':
    paths = ()
    MATCHERS = ['.csv']
    PATH_SRC = '/home/green-machine/books'

    FLAG = ''

    file_names = tuple(filter(lambda _: FLAG in _, os.listdir(PATH_SRC)))

    kwargs = {
        'dir_from': PATH_SRC,
        'dir_to': PATH_SRC,
        'file_names': file_names,
    }

    copy_rename_files(**kwargs)
