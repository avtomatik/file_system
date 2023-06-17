import os
import shutil
from pathlib import Path


def os_walk(PATH_SRC):
    for root, dir, file_names in os.walk(PATH_SRC):
        for file_name in file_names:
            if file_name.endswith(''):
                shutil.copy2(
                Path(root).joinpath(file_name),
                Path(PATH_SRC).joinpath(file_name)
            )