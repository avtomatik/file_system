# =============================================================================
# Separate Procedure
# =============================================================================

import shutil
from pathlib import Path


def incoherent_undefined():
    PATH_BASE = 'C:\\Projects\\Camera'
    FILE_NAME = 'pricesInverse.xlsm'

    PATH = '/media/green-machine/KINGSTON'
    shutil.copy2(
        Path(PATH_BASE).joinpath(FILE_NAME),
        Path(PATH).joinpath(FILE_NAME)
    )

    PATH_EXP = 'E:'
    shutil.copy2(
        Path(PATH_BASE).joinpath(FILE_NAME),
        Path(PATH_EXP).joinpath(FILE_NAME)
    )

    PATH_SRC = 'C:\\Users\\Mastermind\\Desktop'
    PATH_EXP = 'C:\\Projects'
    shutil.move(
        Path(PATH_SRC).joinpath(FILE_NAME),
        Path(PATH_EXP).joinpath(FILE_NAME)
    )

    shutil.make_archive(
        'C:\\Projects\\documents',
        'zip',
        'C:\\Projects\\Documents'
    )
