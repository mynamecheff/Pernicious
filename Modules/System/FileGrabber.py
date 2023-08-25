import os
import shutil

def copy_files_under_size_limit(size_limit):
    extensions = {
        ".txt": "text",
        ".jpg": "images",
        ".png": "images",
        ".db": "database"
    }

    root_directory = os.path.splitdrive(os.getenv("SYSTEMROOT"))[0]
    files = [file for file in get_all_files(root_directory) if is_valid_extension(file) and get_file_size(file) < size_limit * 1024 * 1024]

    for file in files:
        extension = os.path.splitext(file)[1]
        folder = extensions.get(extension, "other")
        new_folder_path = os.path.join(os.getcwd(), folder)
        new_path = os.path.join(new_folder_path, os.path.basename(file))

        # Create the folder if it doesn't exist
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        shutil.copy(file, new_path)

def get_all_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)

def is_valid_extension(file):
    valid_extensions = {".txt", ".jpg", ".png", ".db"}
    return os.path.splitext(file)[1] in valid_extensions

def get_file_size(file):
    return os.path.getsize(file)

if __name__ == "__main__":
    size_limit = 10  # Size limit in megabytes
    copy_files_under_size_limit(size_limit)
