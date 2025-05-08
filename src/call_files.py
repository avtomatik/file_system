#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from pathlib import Path

import pandas as pd
from pandas import DataFrame

from core.config import PATH


def read(filepath: Path) -> DataFrame:
    kwargs = {
        'filepath_or_buffer': filepath,
        'names': ['time_stamp', 'wb_name', 'status'],
        'sep': '\t'
    }
    return pd.read_csv(**kwargs)


def mark_df(df: DataFrame) -> DataFrame:
    df['backed_up'] = False
    df['file_size'] = 0
    return df


if __name__ == '__main__':

    FILE_NAME = 'files_check.txt'

    file_path = PATH.joinpath(FILE_NAME)

    df = read(file_path).pipe(mark_df)

    for _ in range(df.shape[0]):

        filepath = PATH.joinpath(df.iloc[_, 1])

        if filepath.exists():
            df.iloc[_, -2] = filepath.is_file()
            df.iloc[_, -1] = os.stat(filepath).st_size

    FILE_NAME = 'files_check_report.xlsx'

    kwargs = {
        'excel_writer': PATH.joinpath(FILE_NAME),
        'index': False
    }
    df.to_excel(**kwargs)
