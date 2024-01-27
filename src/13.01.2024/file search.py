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


if __name__ == "__main__":
    directory_path = '.'  # Change this to the desired directory path
    files_in_directory = get_files_in_directory(directory_path)

    default_selector = Selector(min_size=10, older_than_days=0, extensions=None)
    filtered_files = filter_files(files_in_directory, default_selector)

    for file in filtered_files:
        print(f"Path: {file.path}, Size: {file.size} B, Last Modify Time: {file.last_modify_time}")
