import os
import shutil
from pathlib import Path

PATH_ROOT_SOURCE = '/media/green-machine/Transcend'
PATH_ROOT_DESTINATION = '/home/green-machine/Downloads'
EXT = '.py'

for root, _dir, file_names in os.walk(PATH_ROOT_SOURCE):
    for file_name in file_names:
        # print(file_name)
        if file_name.endswith(EXT) and not file_name.startswith('~'):
            print(Path(root).joinpath(file_name))

        # if not Path(PATH_ROOT_DESTINATION).joinpath(_file_name).exists():
        #     shutil.move(
        #         Path(root).joinpath(file_name),
        #         Path(PATH_ROOT_DESTINATION).joinpath(_file_name)
        #     )
