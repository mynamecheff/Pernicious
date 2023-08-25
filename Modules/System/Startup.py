import os
import winreg

def add_to_startup(file_path):
    try:
        # Open the registry key
        rk = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_SET_VALUE)

        # Set the value in the registry key
        winreg.SetValueEx(rk, os.path.splitext(os.path.basename(file_path))[0], 0, winreg.REG_SZ, file_path)

        winreg.CloseKey(rk)
        print(f"File '{file_path}' added to startup.")
    except Exception as ex:
        print(f"Error adding file to startup: {ex}")

if __name__ == "__main__":
    file_path = r"C:\Path\To\My\File.exe"  # Replace with your file path
    add_to_startup(file_path)
