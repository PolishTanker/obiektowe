from dataclasses import dataclass
import os
from datetime import datetime, timedelta
from typing import List


@dataclass
class File:
    path: str
    size: int
    last_modify_time: datetime

    def is_older_than(self, days: int) -> bool:
        current_time = datetime.now()
        difference = current_time - self.last_modify_time
        return difference.days > days


@dataclass
class Selector:
    min_size: int = 0
    older_than_days: int = 0
    extensions: List[str] = None


def get_files_in_directory(directory: str) -> List[File]:
    files = []
    for f in os.listdir(directory):
        full_path = os.path.join(directory, f)
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            last_modify_time = datetime.fromtimestamp(os.path.getmtime(full_path))
            files.append(File(path=full_path, size=size, last_modify_time=last_modify_time))
    return files


def filter_files(files: List[File], selector: Selector) -> List[File]:
    filtered_files = []
    for file in files:
        if file.size >= selector.min_size and (selector.older_than_days == 0 or file.is_older_than(selector.older_than_days)):
            if selector.extensions is None or any(file.path.endswith(ext) for ext in selector.extensions):
                filtered_files.append(file)
    return filtered_files


def get_file(full_file: str) -> File:
    if os.path.isfile(full_file):
        size = os.path.getsize(full_file)
        last_modify_time = datetime.fromtimestamp(os.path.getmtime(full_file))
        return File(path=full_file, size=size, last_modify_time=last_modify_time)
    else:
        raise ValueError(f"The provided path '{full_file}' is not a file.")


if __name__ == "__main__":
    # Przykładowa pełna ścieżka do pliku
    full_file_path = './index.html'

    # Uzyskanie obiektu File na podstawie pełnej ścieżki
    file_from_path = get_file(full_file_path)

    # Wydrukowanie informacji o pliku
    print(f"Path: {file_from_path.path}, Size: {file_from_path.size} B, Last Modify Time: {file_from_path.last_modify_time}")
