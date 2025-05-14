from pathlib import Path


def copy_files_to_destination(file_names: tuple[str], path_src: Path, path_dst: Path) -> None:
    for file_name in file_names:
        file_path_src = path_src / file_name
        file_path_dst = path_dst / file_name

        file_path_dst.parent.mkdir(parents=True, exist_ok=True)
        with file_path_src.open('rb') as fsrc, file_path_dst.open('wb') as fdst:
            fdst.write(fsrc.read())

        print(f'Copied <{file_name}> from {path_src} to {path_dst}')


def move_files_to_destination(file_names: tuple[str], path_src: Path, path_dst: Path) -> None:
    path_dst.mkdir(parents=True, exist_ok=True)

    for file_name in file_names:
        src = path_src / file_name
        dst = path_dst / file_name

        src.rename(dst)
        print(f'Moved <{file_name}> from {path_src} to {path_dst}')


def rename_files_based_on_mapping(mapping: dict[str, str], path: Path) -> None:
    for src, dst in mapping.items():
        src_path = path / src
        dst_path = path / dst
        src_path.rename(dst_path)

    print(f'{path}: Done')


def delete_files(file_names: tuple[str], path: Path) -> None:

    for file_name in file_names:
        path.joinpath(file_name).unlink()

    print(f'{path}: Done')
