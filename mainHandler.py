#!/usr/bin/env python3
import shutil
from datetime import date
from pathlib import Path
from extensions import extension_paths


from watchdog.events import FileSystemEventHandler

from AutomaticDesktopCleaner.extensions import extension_paths


def add_date_to_path(path: Path):
    """
    This function creates a folder structure based on the current year and month. 
    It ensures files are organized by the date they are moved.
    If the folders for the year/month don't exist, they are created automatically.
    """
    dated_path = path / f'{date.today().year}' / f'{date.today().month:02d}'
    dated_path.mkdir(parents=True, exist_ok=True)
    return dated_path


def rename_file(source: Path, destination_path: Path):
    """
    Handles naming conflicts by adding an incremented number to the file name 
    if a file with the same name already exists in the destination.
    This prevents overwriting files by accident.
    """
    if Path(destination_path / source.name).exists():
        increment = 0

        while True:
            increment += 1
            new_name = destination_path / f'{source.stem}_{increment}{source.suffix}'

            # Stop when we find a unique file name
            if not new_name.exists():
                return new_name
    else:
        # If no conflict, return the original path
        return destination_path / source.name


class EventHandler(FileSystemEventHandler):
    def __init__(self, watch_path: Path, destination_root: Path):
        """
        Initializes the event handler with the path being watched and the root 
        folder where files should be moved. These paths are resolved to their 
        absolute versions for reliability.
        """
        self.watch_path = watch_path.resolve()
        self.destination_root = destination_root.resolve()

    def on_modified(self, event):
        """
        When a change is detected in the watch folder, this function:
        - Checks all files in the folder.
        - Moves the files with specified extensions to their categorized destinations.
        - Ensures files are organized by date and renamed if necessary.
        """
        for child in self.watch_path.iterdir():
            # Only process files, skip directories or unsupported file extensions
            if child.is_file() and child.suffix.lower() in extension_paths:
                destination_path = self.destination_root / extension_paths[child.suffix.lower()]
                
                # Add the date folder structure and handle file renaming
                destination_path = add_date_to_path(path=destination_path)
                destination_path = rename_file(source=child, destination_path=destination_path)
                
                # Finally, move the file to its new location
                shutil.move(src=child, dst=destination_path)
