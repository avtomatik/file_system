#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 13 10:53:52 2025

@author: alexandermikhailov
"""

import filecmp
from datetime import datetime
from hashlib import md5
from itertools import product
from pathlib import Path

from core.config import PATH, PATH_CTR, PATH_DST, PATH_SRC, PATH_TST


def move_and_replace_files_in_directories():
    # Function to move and replace files between directories
    for file in PATH.iterdir():
        source_file = PATH_CTR.joinpath(file.name)
        destination_file = PATH_TST.joinpath(file.name)

        if filecmp.cmp(source_file, destination_file, shallow=False):
            destination_file.unlink()  # Remove the existing file
            file.rename(destination_file)  # Rename (move) the file


def compare_file_digests_in_directory():
    # Function to calculate and compare digests of two files
    file_digests = []
    for archive_filename in ['project_2022-08-26.tar.gz', 'project_tar.gz']:
        archive_path = PATH.joinpath(archive_filename)
        with open(archive_path, 'rb') as archive_file:
            file_digest = md5(archive_file.read()).hexdigest()
            file_digests.append(file_digest)

    print(file_digests[0] == file_digests[1])


def compare_directories_and_report():
    # Function to compare directories and print the full closure report
    directory_comparison = filecmp.dircmp(PATH_CTR, PATH_TST)
    directory_comparison.report_full_closure()


def count_files_in_directory(directory_path: Path):
    # Function to count the number of files in a specific directory
    return sum(file.is_file() for file in directory_path.rglob('*'))


def remove_matching_files_between_directories():
    # Function to compare files between two directories and remove matching ones
    for source_root, _, source_files in zip(
        (PATH / 'production' / 'egida_ptv' / 'lib').rglob('*'),
        (PATH / 'web' / 'egida_ptv' / 'lib').rglob('*')
    ):
        for source_file, destination_file in zip(sorted(source_files), sorted(_fnames)):
            if filecmp.cmp(source_root / source_file, _rt / destination_file):
                (source_root / source_file).unlink()  # Remove matching file


def remove_empty_directories_in_directory():
    # Function to remove empty directories
    for directory in (PATH / 'production').rglob('*'):
        if not any(directory.iterdir()):  # Check if the directory is empty
            directory.rmdir()  # Remove the empty directory


def get_creation_time(file_path: Path) -> datetime:
    """
    Returns the creation time of the file at the given path.

    :param file_path: Path to the file
    :return: Creation time of the file as a datetime object
    """
    return datetime.fromtimestamp(file_path.stat().st_ctime)


def copy_file(src: Path, dst: Path):
    """
    Copies the file from the source path to the destination path, preserving file metadata.

    :param src: Source file path
    :param dst: Destination file path
    """
    # Read content from source and write to destination
    dst.write_bytes(src.read_bytes())

    # Copy file permissions
    dst.chmod(src.stat().st_mode)

    # Copy access and modification times
    dst.utime((src.stat().st_atime, src.stat().st_mtime))


def sync_files_from_control_to_destination():
    """
    Synchronize files between the control path and the test path by copying the latest file 
    (based on creation time) to the destination and removing files from the source and test path.
    """
    for file_name in sorted(set(PATH_CTR.glob('*')) ^ set(PATH_TST.glob('*'))):
        control_file = PATH_CTR / file_name
        test_file = PATH_TST / file_name
        destination_file = PATH_DST / file_name
        if control_file.is_file():
            if get_creation_time(control_file) <= get_creation_time(test_file):
                copy_file(test_file, destination_file)
            else:
                copy_file(control_file, destination_file)

            control_file.unlink()  # Delete the original file from the control path
            test_file.unlink()  # Delete the original file from the test path


def get_file_names_in_directory(directory: Path) -> list:
    """
    Returns a list of filenames in the specified directory that are files (not directories).

    :param directory: Path to the directory to scan
    :return: List of filenames in the directory
    """
    return [file.name for file in directory.iterdir() if file.is_file()]


def delete_matching_files():
    """
    Deletes files from the source path if they have a matching file in the destination path.
    """
    source_file_names = get_file_names_in_directory(PATH_SRC)
    destination_file_names = get_file_names_in_directory(PATH_DST)

    for source_file, destination_file in product(source_file_names, destination_file_names):
        source_path = PATH_SRC / source_file
        destination_path = PATH_DST / destination_file

        if filecmp.cmp(source_path, destination_path, shallow=False):
            source_path.unlink()  # Delete matching file from source
            print(f'Deleted {source_path} as it matches {destination_path}')


# =============================================================================
# Constants
# =============================================================================
RESERVED = {'FOUND.000', 'System Volume Information'}


# =============================================================================
# Helper Functions
# =============================================================================

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


def copy_empty_files(file_names: list, src_path: Path, dst_path: Path) -> None:
    """
    Copy empty files from source to destination if they exist.

    :param file_names: List of file names to copy.
    :param src_path: Path to the source directory.
    :param dst_path: Path to the destination directory.
    """
    for filename in file_names:
        src_file = src_path / filename
        dst_file = dst_path / filename

        if src_file.exists() and src_file.is_file():
            dst_file.write_bytes(src_file.read_bytes())
            print(f'Copied <{filename}> from {src_path} to {dst_path}')


def backup_files(PATH_SRC: Path, PATH_DST: Path, PREFIXES: set, SUFFIX: str) -> None:
    """
    Backup files from the source directory to the destination directory based on specific conditions.

    :param PATH_SRC: Path to the source directory.
    :param PATH_DST: Path to the destination directory.
    :param PREFIXES: Set of file name prefixes to exclude.
    :param SUFFIX: File suffix (e.g., '.py') to filter the files by.
    """
    for path in PATH_SRC.rglob('*'):
        if not path.is_file():
            continue

        file_name = path.name
        file_name_dst = PATH_SRC / file_name

        # Copy to PATH_SRC if valid (ends with SUFFIX and does not start with a prefix)
        if file_name.endswith(SUFFIX) and not file_name.startswith(tuple(PREFIXES)):
            file_name_dst.write_bytes(path.read_bytes())
        # Copy to PATH_DST if not already present
        file_name_dst = PATH_DST / file_name
        if not file_name_dst.exists():
            file_name_dst.write_bytes(path.read_bytes())
            path.unlink()
