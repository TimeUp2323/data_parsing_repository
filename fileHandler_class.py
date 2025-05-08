import os
from file_class import File


class FileHandler:
    def __init__(self):
        self._count_files = 0
        self._extensions = {}

    def process_all_directories(self, path: str) -> None:
        self._count_files = 0
        self._extensions = {}
        self._walk_current_directory(path)

    def _walk_current_directory(self, folder_path: str) -> None:
        try:
            for item in os.listdir(folder_path):
                path = os.path.join(folder_path, item)
                if os.path.isfile(path):
                    self._process_file(path)
                else:
                    self._walk_current_directory(path)
        except PermissionError:
            raise RuntimeError(f"Требуются права администратора для: {folder_path}")
        except Exception as e:
            raise RuntimeError(f"Ошибка обработки директории: {str(e)}")

    def _process_file(self, file_path: str) -> None:
        file = File(file_path)
        self._count_extensions(file.get_extension())

    def _count_extensions(self, ext: str) -> None:
        self._extensions[ext] = self._extensions.get(ext, 0) + 1
        self._count_files += 1

    def get_extensions(self) -> dict:
        return self._extensions.copy()

    def get_count_files(self) -> int:
        return self._count_files