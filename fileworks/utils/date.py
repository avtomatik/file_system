from datetime import datetime
from pathlib import Path


def get_creation_time(file_path: Path) -> datetime:
    """
    Returns the creation time of the file at the given path.

    :param file_path: Path to the file
    :return: Creation time of the file as a datetime object
    """
    return datetime.fromtimestamp(file_path.stat().st_ctime)
