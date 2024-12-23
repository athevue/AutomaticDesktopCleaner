#! /usr/bin/env python3

from mainHandler import EventHandler
from pathlib import Path
from time import sleep

from watchdog.observers import Observer

from AutomaticDesktopCleaner.mainHandler import EventHandler

if __name__ == '__main__':
    # Set up the folder to watch (the Desktop in this case)
    watch_path = Path.home() / 'Desktop'

    # Define where files should be moved (a subfolder in the Desktop)
    destination_root = Path.home() / 'Desktop/holder of things'

    # Create an instance of the EventHandler to handle file events
    event_handler = EventHandler(watch_path=watch_path, destination_root=destination_root)

    # Set up the Observer to watch the folder for changes
    observer = Observer()

    # Schedule the observer to monitor the watch_path for file modifications
    # Recursive=True ensures it monitors subdirectories too
    observer.schedule(event_handler, f'{watch_path}', recursive=True)

    # Start the observer so it actively listens for changes
    observer.start()

    try:
        # Keep the program running indefinitely so it can keep monitoring
        while True:
            sleep(60)  # Wait for 60 seconds before checking again
    except KeyboardInterrupt:
        # If the user interrupts (Ctrl+C), stop the observer gracefully
        observer.stop()
    # Wait for the observer to completely shut down before exiting
    observer.join()
