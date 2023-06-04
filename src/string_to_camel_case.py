import os
import re

PATH_SRC = '/home/green-machine/data_science/src'
file_names = tuple(os.listdir(PATH_SRC))
map_file_names = {
    _: re.sub(r'(?<!^)(?=[A-Z])', '_', _).lower() for _ in file_names
}
