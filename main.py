import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter as tk
from tkinter import filedialog
import os

class Watcher:
    def __init__(self, directory_to_watch):
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        print(f"Created: {os.path.basename(event.src_path)}")

    @staticmethod
    def on_modified(event):
        print(f"Modified: {os.path.basename(event.src_path)}")

    @staticmethod
    def on_moved(event):
        print(f"Renamed: {os.path.basename(event.src_path)} -> {os.path.basename(event.dest_path)}")

def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    folder_selected = filedialog.askdirectory()  # Open the folder selection dialog
    return folder_selected

if __name__ == "__main__":
    print("Select a folder to watch...")
    directory = select_directory()
    print(f"Watching directory: {directory}")
    w = Watcher(directory)
    w.run()
