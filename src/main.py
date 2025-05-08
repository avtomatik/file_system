#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 17:06:20 2022

@author: Alexander Mikhailov
"""

from pathlib import Path

from core.config import PATH
from core.funcs import move_and_rename_files

MATCHERS = ('.csv',)
MATCHERS = ('',)


def is_target(f: Path, matchers: tuple[str], flag: str = '') -> bool:
    return flag in f.name and f.suffix in matchers


if __name__ == '__main__':
    file_names = tuple(
        f.name for f in PATH.iterdir() if is_target(f, MATCHERS)
    )

    file_names = tuple(f.name for f in PATH.iterdir())

    kwargs = {
        'path_src': PATH,
        'path_dst': PATH,
        'file_names': file_names,
    }

    move_and_rename_files(**kwargs)
