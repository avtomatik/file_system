import datetime
import io
import os
import re
import shutil
from pathlib import Path

from core.constants import MAP_CYRILLIC_TO_LATIN

# from strings.src.lib import trim_string


def trim_string(string: str, fill: str = ' ') -> str:
    return fill.join(filter(bool, re.split(r'\W', string)))


def get_set_from_text_file(file_name: str) -> set:
    with io.open(file_name, mode='r', encoding='utf-8') as f:
        return set(map(str.lower, map(str.rstrip, f.readlines())))


def transliterate(word: str, mapping: dict[str] = MAP_CYRILLIC_TO_LATIN) -> str:
    return ''.join(
        mapping[_.lower()] if _.lower() in mapping.keys() else _ for _ in word
    )


def trim_file_name(file_name: str) -> str:
    _file_name = f"{trim_string(Path(file_name).stem, '_')}{Path(file_name).suffix}"
    return transliterate('_'.join(filter(bool, _file_name.lower().split('_'))))


def get_file_names(matchers: tuple[str]) -> list[str]:
    return [
        file_name for file_name in tuple(os.listdir()) if any(match in file_name for match in matchers)
    ]


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

    # filepath = Path(PATH_LOG).joinpath(FILE_NAME_LOG)
    # with open(filepath, 'w') as f:
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


def get_file_names_set(path):
    return set(map(str.lower, os.listdir(path)))


def files_mirroring(paths: tuple[str], file_names: tuple[str]) -> None:
    file_names_one = get_set_from_text_file(file_names[0])
    file_names_two = get_set_from_text_file(file_names[1])

    file_names_diff = file_names_one - file_names_two

    for file_name in file_names_diff:
        shutil.copy2(
            Path(paths[0]).joinpath(file_name),
            Path(paths[1]).joinpath(file_name)
        )
        print(f'Copied {file_name}')

    file_names_diff = file_names_two - file_names_one

    for file_name in file_names_diff:
        shutil.copy2(
            Path(paths[1]).joinpath(file_name),
            Path(paths[0]).joinpath(file_name)
        )
        print(f'Copied {file_name}')
