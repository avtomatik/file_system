#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# =============================================================================
# TODO: Drop Drives in Paths
# =============================================================================
from pathlib import Path

from core.config import PATH_DST, PATH_SRC, PATH_TST
from core.constants import FILE_NAME_DST, FILE_NAME_SRC
from core.helpers import get_string_from_file, trim_file_name

file_names_src = get_string_from_file(FILE_NAME_SRC)
file_names_dst = get_string_from_file(FILE_NAME_DST)

max_len = max(len(file_names_src), len(file_names_dst))
file_names_src += ['None'] * (max_len - len(file_names_src))
file_names_dst += ['None'] * (max_len - len(file_names_dst))

rows = list(zip(file_names_src, file_names_dst))

MAP_RENAMING = {
    # status would have been 'None'
    dst: src for src, dst in rows if 'None' in (src, dst)
}


# =============================================================================
# Iteration
# =============================================================================
for file_name in MAP_RENAMING.keys():
    src = Path(file_name)
    dst = Path(trim_file_name(file_name))
    if src.exists() and not dst.exists():
        src.rename(dst)

# =============================================================================
# Iteration
# =============================================================================
for file_name_src, file_name_dst in MAP_RENAMING.items():
    action = file_name_src
    src = file_name_dst
    dst = trim_file_name(src)

    if action == f'{PATH_TST} TO {PATH_SRC}':
        src_path = Path(src)
        src_relative_path = src_path.relative_to(src_path.drive)

        dst_path = Path(dst)
        dst_relative_path = dst_path.relative_to(dst_path.drive)

        print(f'{src_relative_path} {dst_relative_path}')

        if src_relative_path.exists() and not dst_relative_path.exists():
            src_relative_path.rename(dst_relative_path)

    elif action == f'{PATH_SRC} TO {PATH_DST}':
        print(f'{dst} {src}')
