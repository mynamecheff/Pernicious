import os
import plistlib
import base64
from xml.etree import ElementTree as ET

config_path = os.path.join(os.environ['APPDATA'], 'Cyberduck', 'Bookmarks.plist')

if not os.path.exists(config_path):
    print("Cyberduck configuration file not found!")
    exit()

hosts = []

with open(config_path, 'rb') as plist_file:
    plist_data = plistlib.load(plist_file)

for bookmark in plist_data:
    if bookmark.get('Protocol') == 'ftp':
        host = bookmark['Hostname']
        username = bookmark['Username']
        password = base64.b64decode(bookmark['Password']).decode('utf-8')

        url = f"ftp://{host}/"
        credentials = f"Url: {url}\nUsername: {username}\nPassword: {password}\n\n"
        hosts.append(credentials)

if hosts:
    save_path = "Cyberduck.txt"
    with open(save_path, 'w') as file:
        file.writelines(hosts)
    print(f"Found {len(hosts)} Cyberduck hosts and saved to {save_path}")
else:
    print("No Cyberduck hosts found.")
