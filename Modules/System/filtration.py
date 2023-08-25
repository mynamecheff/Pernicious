import subprocess
import socket
import os
import sys
import psutil

#Detect Vm
def is_running_in_virtual_machine():
    system_manufacturer = subprocess.check_output(["wmic", "computersystem", "get", "Manufacturer"]).decode("utf-8").strip()
    system_model = subprocess.check_output(["wmic", "computersystem", "get", "Model"]).decode("utf-8").strip()
    video_controller_name = subprocess.check_output(["wmic", "path", "win32_videocontroller", "get", "Name"]).decode("utf-8").strip()
    return "vmware" in system_manufacturer.lower() or \
           ("virtual" in system_model.lower() and system_manufacturer.lower() == "microsoft corporation") or \
           ("vmware" in video_controller_name.lower() and "vbox" in video_controller_name.lower())
    
print("is it a VM? " + str(is_running_in_virtual_machine()))

# Detect if scanner
def is_scanner():
    try:
        host_name = socket.gethostname()
        ip_addresses = socket.gethostbyname_ex(host_name)[2]

        for ip_address in ip_addresses:
            if ip_address.startswith(("192.168.", "10.", "172.")):
                continue
            elif ip_address == "127.0.0.1" or ip_address == "::1":
                continue
            elif any(keyword in host_name for keyword in ["virustotal", "any.run", "hybrid-analysis", "metadefender", "joesecurity"]):
                return True
            elif ip_address.startswith("104.16.") or ip_address.startswith("104.20.") or ip_address.startswith("104.31."):
                return True
    except:
        pass
    return False

print("is it a scanner? " + str(is_scanner()))


# Prevent multiple instances
def prevent_multiple_instances():
    process_name = os.path.basename(sys.argv[0])
    existing_processes = [p for p in psutil.process_iter(attrs=['pid', 'name']) if p.info['name'] == process_name]

    if len(existing_processes) > 1:
        print("Another instance of the program is already running.")
        input()
        sys.exit()

    print("Program is running.")

prevent_multiple_instances()