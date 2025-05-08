import os
import shutil
from pathlib import Path

from core.config import PATH_DST, PATH_SRC
from core.constants import PREFIXES

SUFFIX = '.py'


for root, _, file_names in os.walk(PATH_SRC):
    for file_name in file_names:

        _file_name = ''

        if file_name.endswith(SUFFIX) and not file_name.startswith(PREFIXES):
            print(Path(root).joinpath(file_name))
            shutil.copy2(
                Path(root).joinpath(file_name),
                PATH_SRC.joinpath(file_name)
            )

        if not PATH_DST.joinpath(_file_name).exists():
            shutil.move(
                Path(root).joinpath(file_name),
                PATH_DST.joinpath(_file_name)
            )
