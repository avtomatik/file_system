#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from pathlib import Path

import pandas as pd
from core.config import PATH
from pandas import DataFrame


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

        file_path = PATH.joinpath(df.iloc[_, 1])

        if file_path.exists():
            df.iloc[_, -2] = file_path.is_file()
            df.iloc[_, -1] = os.stat(file_path).st_size

    FILE_NAME = 'files_check_report.xlsx'

    file_path = PATH.joinpath(FILE_NAME)

    kwargs = {
        'excel_writer': file_path,
        'index': False
    }
    df.to_excel(**kwargs)
