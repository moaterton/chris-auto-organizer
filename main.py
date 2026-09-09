import os
import shutil
import time
import sys

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, DirModifiedEvent, FileModifiedEvent

print("Initializing Auto Organizer.")

time.sleep(1)

print("Press Enter to start.")

user_input = input()

if user_input == "":
    downloads_fldr = os.path.expanduser("~/Downloads")
    dest_documents_downloads = os.path.expanduser("~/Documents/Downloads")
    dest_compressed_files = os.path.expanduser("~/Documents/Downloads/Compressed_Files")
    dest_roblox_place_files = os.path.expanduser("~/Documents/Downloads/Roblox_Files/Games")
    dest_roblox_asset_files = os.path.expanduser("~/Documents/Downloads/Roblox_Files/Assets")
    dest_video_files = os.path.expanduser("~/Documents/Downloads/Videos&Sounds/Videos")
    dest_sound_files = os.path.expanduser("~/Documents/Downloads/Videos&Sounds/Sounds")
    dest_executable_files = os.path.expanduser("~/Documents/Downloads/Executables")
    dest_configuration_files = os.path.expanduser("~/Documents/Downloads/Configs")
    dest_image_files = os.path.expanduser("~/Documents/Downloads/Images")

    compressed_file_types = [  # Finished
        ".zip",
        ".7z",
        ".rar",
        ".xz",
        ".bz2",
    ]

    video_types = [  # Finished
        ".mp4",
        ".mov",
        ".mkv",
        ".webm",
        ".wmv"
    ]

    sound_types = [  # Finished
        ".wav",
        ".mp3",
        ".ogg"
    ]

    configuration_types = [  # Finished
        ".json",
        ".toml",
        ".txt",
    ]

    image_types = [  # Finished
        ".jpeg",
        ".jpg",
        ".png",
    ]

    game_file_types = [
        ".json",
        ".toml",
    ]

    roblox_place_type = [".rbxl"]  # Finished
    roblox_asset_type = [".rbxm"]  # Finished
    executable_asset_type = [".exe"]  # Finished


    def make_dirs(path):
        if not path:
            return

        os.makedirs(path, exist_ok=True)


    def move_entry(t, dest, file_name, source_path):
        for ext in t:
            if file_name.endswith(ext):
                dest_folder = dest
                dest_path = os.path.join(dest_folder, file_name)

                os.makedirs(dest_folder, exist_ok=True)

                try:
                    shutil.move(source_path, dest_path)
                    print(f"Successfully moved {file_name} to {dest_path}")
                except Exception as e:
                    print(f"Error moving {file_name}: {e}")


    make_dirs(dest_documents_downloads)
    make_dirs(dest_compressed_files)
    make_dirs(dest_roblox_place_files)
    make_dirs(dest_roblox_asset_files)
    make_dirs(dest_video_files)
    make_dirs(dest_sound_files)
    make_dirs(dest_executable_files)
    make_dirs(dest_configuration_files)
    make_dirs(dest_image_files)


    class FolderMonitorHandler(FileSystemEventHandler):
        def on_created(self, event):
            print(f"Created: {event.src_path}")
            if event.is_directory:
                return

            source_path = event.src_path
            file_name = os.path.basename(source_path)

            move_entry(compressed_file_types, dest_compressed_files, file_name, source_path)

            move_entry(roblox_place_type, dest_roblox_place_files, file_name, source_path)

            move_entry(roblox_asset_type, dest_roblox_asset_files, file_name, source_path)

            move_entry(video_types, dest_video_files, file_name, source_path)

            move_entry(sound_types, dest_sound_files, file_name, source_path)

            move_entry(executable_asset_type, dest_executable_files, file_name, source_path)

            move_entry(configuration_types, dest_configuration_files, file_name, source_path)

            move_entry(image_types, dest_image_files, file_name, source_path)

        def on_deleted(self, event):
            print(f"Deleted: {event.src_path}")

        def on_modified(self, event):
            print(f"Modified: {event.src_path}")

        def on_moved(self, event):
            print(f"Moved: {event.src_path}")


    if __name__ == "__main__":
        folder_to_watch = os.path.expanduser("~/Downloads")

        event_handler = FolderMonitorHandler()
        observer = Observer()
        observer.schedule(event_handler, path=folder_to_watch, recursive=False)

        print(f"Watching for changes in: {folder_to_watch}")
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopping monitor...")
            observer.stop()

        observer.join()