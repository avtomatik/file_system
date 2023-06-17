# =============================================================================
# Separate Procedure
# =============================================================================

import shutil
from pathlib import Path


def incoherent_undefined():
    PATH_BASE = 'C:\\Projects\\Camera'
    FILE_NAME = 'pricesInverse.xlsm'

    PATH = '/media/green-machine/KINGSTON'
    shutil.copy(
        Path(PATH_BASE).joinpath(FILE_NAME),
        Path(PATH).joinpath(FILE_NAME)
    )

    shutil.copy(
        Path(PATH_BASE).joinpath(FILE_NAME),
        Path('E:').joinpath(FILE_NAME)
    )

    shutil.move(
        Path('C:\\Users\\Mastermind\\Desktop').joinpath(FILE_NAME),
        Path('C:\\Projects').joinpath(FILE_NAME)
    )

    shutil.make_archive(
        'C:\\Projects\\documents',
        'zip',
        'C:\\Projects\\Documents'
    )
