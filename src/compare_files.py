#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 19:23:12 2024

@author: alexandermikhailov
"""

import filecmp
import os
import shutil
from pathlib import Path

PATH_C = '/Volumes/Samsung USB/web/egida_ptv/'
PATH_T = '/Volumes/Samsung USB/production/egida_ptv/'

PATH_BASE = '/Volumes/Samsung USB'


# =============================================================================
# for file_name in os.listdir(PATH_C):
#     if filecmp.cmp(
#         Path(PATH_C).joinpath(file_name),
#         Path(PATH_T).joinpath(file_name),
#         shallow=False
#     ):
#         Path(PATH_T).joinpath(file_name).unlink()
#         shutil.move(
#             Path(PATH_C).joinpath(file_name),
#             Path(PATH_T).joinpath(file_name),
#         )
# =============================================================================

# =============================================================================
# from hashlib import md5
# digests = list()
# os.chdir(PATH)
# for filename in ['project_2022-08-26.tar.gz', 'project_tar.gz']:
#     with open(filename, 'rb') as f:
#         digest = md5(f.read()).hexdigest()
#         digests.append(digest)

# print(digests[0] == digests[1])
# =============================================================================

# =============================================================================
# comparison = filecmp.dircmp(Path(PATH_C), Path(PATH_T))
# comparison.report_full_closure()
# =============================================================================

# =============================================================================
# count = []
#
# for root, _, file_names in os.walk(
#     (
#         Path(PATH_BASE)
#         .joinpath('production')
#         .joinpath('egida_ptv')
#         .joinpath('lib')
#     )
# ):
#     for file_name in file_names:
#         count.append(Path(root).joinpath(file_name).is_file())
#
# print(sum(count))
# =============================================================================

# =============================================================================
# for (rt, _, fnames), (_rt, _, _fnames) in zip(
#     os.walk(Path(PATH_BASE).joinpath('production').joinpath(
#         'egida_ptv').joinpath('lib')),
#     os.walk(Path(PATH_BASE).joinpath('web').joinpath(
#         'egida_ptv').joinpath('lib'))
# ):
#     for f, _f in zip(sorted(fnames), sorted(_fnames)):
#         if filecmp.cmp(Path(rt).joinpath(f), Path(_rt).joinpath(_f)):
#             Path(rt).joinpath(f).unlink()
# =============================================================================

# =============================================================================
# for rt, _, fnames in os.walk(Path(PATH_BASE).joinpath('production')):
#     if not any(Path(rt).iterdir()):
#         Path(rt).rmdir()
# =============================================================================
