from watcher import Watcher
from directory_selector import select_directory

if __name__ == "__main__":
    print("Select a folder to watch...")
    directory = select_directory()
    print(f"Watching directory: {directory}")
    w = Watcher(directory)
    w.run()