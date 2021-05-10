import os


def get_directory_size(path: str) -> int:
    """Returns folder size in bytes. Blocking function."""
    size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            size += os.stat(os.path.join(dirpath, f)).st_size
    return size
