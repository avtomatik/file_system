#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os

import pandas as pd
from lib import trim_file_name
from pandas import DataFrame

# =============================================================================
# TODO: Edit This
# =============================================================================

FILE_NAMES = (
    'file_names_d.txt',
    'file_names_e.txt',
)
FILE_NAME = 'file_names.xlsx'
# =============================================================================
# Iteration
# =============================================================================
with open(FILE_NAMES[0]) as f:
    lines_d = [line.rstrip() for line in f]

with open(FILE_NAMES[1]) as f:
    lines_e = [line.rstrip() for line in f]

pd.concat(
    [
        DataFrame(data={'lines_d': lines_d}),
        DataFrame(data={'lines_e': lines_e})
    ],
    axis=0).to_excel(FILE_NAME)

# =============================================================================
# Iteration
# =============================================================================
for file_name in tuple(os.listdir()):
    os.rename(
        file_name,
        trim_file_name(file_name)
    )

df = pd.read_excel(FILE_NAME)
df.columns = ('lines_d', 'lines_e', 'status')
df.fillna('None', inplace=True)
df.to_excel(FILE_NAME)

# =============================================================================
# Iteration
# =============================================================================
df = pd.read_excel(FILE_NAME)
df = df[df.iloc[:, 2] == 'None'][df.columns[[1, 0]]]
MAP_RENAMING = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))
# =============================================================================
# Iteration
# =============================================================================

for file_name in MAP_RENAMING.keys():
    try:
        os.rename(
            file_name,
            trim_file_name(file_name)
        )
    except:
        pass

for _ in range(df.shape[0]):
    if df.iloc[_, 0] == 'E TO D':
        print('{} {}'.format(df.iloc[_, 1][3:], df.iloc[_, 2][3:]))
        try:
            os.rename(df.iloc[_, 1][3:], df.iloc[_, 2][3:])
        except:
            pass
    elif df.iloc[_, 0] == 'E TO D':
        print('{} {}'.format(df.iloc[_, 2], df.iloc[_, 1]))
