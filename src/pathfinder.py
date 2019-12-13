import os
from pathlib import Path

from consts import Platform


class PathFinder(object):
    def __init__(self, system):
        if system == Platform.WINDOWS:
            self.is_exe = self.__is_windows_exe
        else:
            self.is_exe = self.__is_posix_exe

    def find_executables(self, folder):
        folder = Path(folder)
        if not folder.exists():
            raise FileNotFoundError(f'pathfinder: {folder} does not exist')
        execs = [] 
        for root, dirs, files in os.walk(folder):
            for path in files:
                whole_path = os.path.join(root, path)
                if self.is_exe(whole_path):
                    execs.append(whole_path)
        return execs
    
    def __is_windows_exe(self, path):
        return path.endswith('.exe')

    def __is_posix_exe(self, path):
        return os.access(path, os.X_OK)
