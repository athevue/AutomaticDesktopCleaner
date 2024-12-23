# AutomaticDesktopCleaner
AutomaticDesktopCleaner is a Python tool that automatically organizes files on your desktop by type. It watches for changes and moves files into categorized folders by extension, while creating subfolders by year and month. It also renames files to avoid overwriting if duplicates are found. Simple and effective desktop cleanup.

Key Features:
Automatically detects changes on your desktop.
Moves files to designated directories based on file types.
Customizable folder paths for better organization.
Real-time file watching and organization using watchdog library.

Technologies Used:
Python 3
watchdog library for file system monitoring
Pathlib for directory management

Installation:
Clone the repository: git clone https://github.com/athevue/AutomaticDesktopCleaner.git
Install dependencies: pip install -r requirements.txt
Run the script: python automatic_desktop_cleaner.py

How It Works:
Watches your desktop directory for any new or modified files.
Automatically moves them to specific directories based on the file type (e.g., documents, images, videos).
