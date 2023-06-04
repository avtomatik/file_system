import datetime
import io
import os
import re
import shutil
from os.path import splitext
from pathlib import Path

from constants import LATIN_SUBSTITUTION

MAP_CYRILLIC_TO_LATIN = {
    chr(_): latin for _, latin in enumerate(LATIN_SUBSTITUTION.split(","), start=1072)
}


def get_set_from_text_file(file_name: str) -> set:
    with io.open(file_name, mode='r', encoding='utf-8') as f:
        return {line.rstrip().lower() for line in f.readlines()}


def transliterate(word: str, mapping: dict[str] = MAP_CYRILLIC_TO_LATIN) -> str:
    return ''.join(
        mapping[_.lower()] if _.lower() in mapping.keys() else _ for _ in word
    )


def trim_string(string: str, fill: str = ' ') -> str:
    return fill.join(filter(bool, re.split(r'\W', string)))


def trim_file_name(file_name: str) -> str:
    _file_name = ''.join(
        (trim_string(splitext(file_name)[0], '_').lower(),
         splitext(file_name)[1].lower(),)
    )
    return transliterate('_'.join(p for p in _file_name.split('_') if p))


def get_file_names(matchers):
    return [name for name in tuple(os.listdir()) if any(match in name for match in matchers)]


def copy_rename_files(dir_from: str, dir_to: str, file_names: tuple[str]) -> None:
    """
    Copies <shutil.copy2> or Moves <shutil.move> Files
    Parameters
    ----------
    dir_from : str
        Source Directory.
    dir_to : str
        Destination Directory.
    file_names : tuple[str]
        File Names Set.
    Returns
    -------
    None
    """
    os.chdir(dir_from)
    PATH_LOG = '/home/green-machine/Downloads'
    FILE_NAME_LOG = f'log_{datetime.datetime.today()}.txt'.replace(' ', '_')
    LOG = []
    for file_name in file_names:
        try:
            shutil.move(
                Path(dir_from).joinpath(file_name),
                Path(dir_to).joinpath(trim_file_name(file_name))
            )
        except:
            pass
        # =====================================================================
        # Logging
        # =====================================================================
        LOG.append(
            {
                'from': file_name,
                'to': trim_file_name(file_name),
            }
        )
    # with open(Path(PATH_LOG).joinpath(FILE_NAME_LOG), 'w') as f:
    #     json.dump(LOG, f, ensure_ascii=False)
    print(f'Moved {len(LOG)} Files')


def delete_files(file_names: tuple[str], path: str) -> None:
    for file_name in file_names:
        os.unlink(Path(path).joinpath(file_name))

    print(f'{path}: Done')


def rename_files(mapping: dict[str, str], path: str) -> None:
    for fn_in, fn_ut in mapping.items():
        os.rename(
            Path(path).joinpath(fn_in),
            Path(path).joinpath(fn_ut)
        )

    print(f'{path}: Done')


def move_files(file_names: tuple[str], path_from: str, path_to: str) -> None:
    path_from = '/Users/alexandermikhailov/Documents'
    path_to = '/Volumes/NO NAME/'
    path_to = '/Volumes/NO NAME 1/'
    os.chdir(path_from)
    for file_name in file_names:
        shutil.copy2(
            Path(path_from).joinpath(file_name),
            Path(path_to).joinpath(file_name)
        )
        shutil.move(
            Path(path_from).joinpath(file_name),
            Path(path_to).joinpath(file_name)
        )

    print('Done')


def get_names(PATH_SRC):
    return map(lambda _: _[1:], os.walk(PATH_SRC))


def text_file_to_set(file_name: str) -> set:
    with io.open(file_name, mode='r', encoding='utf-8') as file:
        return {line.rstrip().lower() for line in file.readlines()}


def get_file_names_set(path):
    return {file_name.lower() for file_name in os.listdir(path)}
