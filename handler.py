from watchdog.events import FileSystemEventHandler
import os

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