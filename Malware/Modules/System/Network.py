import psutil
import os
import getpass
import winreg
import socket
import requests
import subprocess
import re
from xml.etree import ElementTree as ET

# Network information
def format_bytes(bytes):
    sizes = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while bytes >= 1024 and i < len(sizes) - 1:
        bytes /= 1024
        i += 1
    return f"{bytes:.2f} {sizes[i]}"

adapters = psutil.net_if_stats()
print("Network Interfaces:")
for adapter_name, stats in adapters.items():
    print(f"   Name: {adapter_name}")
    print(f"   Is Up: {stats.isup}")
    print(f"   Speed: {format_bytes(stats.speed)}")
    print()

addresses = psutil.net_if_addrs()
for adapter_name, adapter_addrs in addresses.items():
    for addr in adapter_addrs:
        print(f"   Interface: {adapter_name}")
        print(f"   Address Family: {addr.family.name}")
        print(f"   Address: {addr.address}")
        if addr.broadcast:
            print(f"   Broadcast: {addr.broadcast}")
        if addr.netmask:
            print(f"   Netmask: {addr.netmask}")
        print()

print()

# Basic user information
user_name = getpass.getuser()
user_domain = os.environ.get('USERDOMAIN')

print("User Profile Information:")
print(f"   Name: {user_name}")
print(f"   Domain: {user_domain}")
print()

# Detailed user information
user_info = os.getlogin()
print("Detailed User Profile Information:")
print(f"   User Info: {user_info}")
print()

# Read registry key (work in progress)
# key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
# sub_key = "SomeExampleApp"

# try:
#     with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) as reg_key:
#         value = winreg.QueryValueEx(reg_key, sub_key)[0]
#         print(f"{sub_key} registry value: {value}")
# except FileNotFoundError:
#     print(f"{sub_key} registry value not found.")

# Internal IP Address
internal_ip = socket.gethostbyname(socket.gethostname())
print(f"Internal IP Address: {internal_ip}")

# External IP Address
external_ip_raw = requests.get("https://ifconfig.me/ip").text.strip()
print(f"External IP Address: {external_ip_raw}")

#wifi passwords
command_output = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8")
profile_names = re.findall("All User Profile\s+:\s(.*)", command_output)

wifi_passwords = {}
for profile_name in profile_names:
    try:
        password_output = subprocess.check_output(["netsh", "wlan", "show", "profile", profile_name, "key=clear"]).decode("utf-8")
        password = re.search("Key Content\s+:\s(.*)", password_output)[1]
        wifi_passwords[profile_name] = password
    except subprocess.CalledProcessError:
        pass

for ssid, password in wifi_passwords.items():
    print(f"SSID: {ssid}, Password: {password}")

# current location
url = f"http://www.geoplugin.net/xml.gp"

response = requests.get(url)
xml_data = ET.fromstring(response.text)

city = xml_data.find("geoplugin_city").text
region = xml_data.find("geoplugin_region").text
country = xml_data.find("geoplugin_countryName").text
latitude = float(xml_data.find("geoplugin_latitude").text)
longitude = float(xml_data.find("geoplugin_longitude").text)

print(f"City: {city}")
print(f"Region: {region}")
print(f"Country: {country}")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")