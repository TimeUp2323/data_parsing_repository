import os


class File:
    def __init__(self, path: str):
        self._path = path
        self._name = os.path.basename(path)
        self._extension = os.path.splitext(path)[1]

    def get_name(self) -> str:
        return self._name

    def get_extension(self) -> str:
        return self._extension