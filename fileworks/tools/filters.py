from pathlib import Path

from core.constants import PREFIXES


def get_files_excluding(name_excluded: str, folder_str=None) -> list[str]:
    path = Path(folder_str or '.')
    return [
        file.name
        for file in path.iterdir()
        if file.is_file() and file.name != name_excluded
    ]


def get_filtered_file_names(prefixes: set[str] = PREFIXES, folder_str=None) -> list[str]:
    # W0102
    path = Path(folder_str or '.')
    return [
        file.name.lower()
        for file in path.iterdir()
        if file.is_file() and not any(
            file.name.lower().startswith(prefix) for prefix in prefixes
        )
    ]


def get_files_matching_all_patterns(matchers: tuple[str], folder_str=None) -> list[str]:
    path = Path(folder_str or '.')
    return [
        file.name
        for file in path.iterdir()
        if file.is_file() and all(matcher in file.name for matcher in matchers)
    ]


def get_files_matching_any_pattern(matchers: tuple[str], folder_str=None) -> list[str]:
    path = Path(folder_str or '.')
    return [
        file.name
        for file in path.iterdir()
        if file.is_file() and any(matcher in file.name for matcher in matchers)
    ]


def get_file_names(path: Path) -> list[str]:
    return [f.name.lower() for f in path.iterdir() if f.is_file()]


def walk_and_list_directory(path: Path):
    result = []
    for path in path.rglob('*'):
        if path.is_dir():
            dirnames = [p.name for p in path.iterdir() if p.is_dir()]
            filenames = [p.name for p in path.iterdir() if p.is_file()]
            result.append((dirnames, filenames))
    return result


def get_empty_files(path: Path, reserved: set) -> list:
    """
    Retrieve a list of file names that are empty and not in the reserved set.

    :param path: Path to the directory where the files are located.
    :param reserved: Set of reserved file names that should be excluded.
    :return: List of empty file names.
    """
    empty_file_names = []
    for file in path.iterdir():
        if file.is_file() and file.stat().st_size == 0 and file.name not in reserved:
            empty_file_names.append(file.name)
    return empty_file_names


def get_file_names_in_directory(directory: Path) -> list:
    """
    Returns a list of filenames in the specified directory that are files (not directories).

    :param directory: Path to the directory to scan
    :return: List of filenames in the directory
    """
    return [file.name for file in directory.iterdir() if file.is_file()]
