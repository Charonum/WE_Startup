import sys
import subprocess
import os
import zipfile
import shutil
import ctypes
import wget

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

if not ctypes.windll.shell32.IsUserAnAdmin():
    import sys
    ctypes.windll.shell32.ShellExecuteW(
        None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
    exit(0)
else:
    pass


try:
    os.mkdir(rf"C:\Program Files\Charonum\Wrigley Engine")
except:
    pass

subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

url = "https://github.com/Charonum/WE_Startup/archive/refs/heads/main.zip"
wget.download(url, rf"C:\Program Files\Charonum\Wrigley Engine")

with zipfile.ZipFile(rf"C:\Program Files\Charonum\Wrigley Engine\WE_Startup-main.zip", 'r') as zipObj:
    zipObj.extractall(rf"C:\Program Files\Charonum\Wrigley Engine")

for file in os.listdir(rf"C:\Program Files\Charonum\Wrigley Engine\WE_Startup-main"):
    shutil.move(rf"C:\Program Files\Charonum\Wrigley Engine\WE_Startup-main\{file}", rf"C:\Program Files\Charonum\Wrigley Engine")

os.remove(rf"C:\Program Files\Charonum\Wrigley Engine\WE_Startup-main.zip")
os.remove(rf"C:\Program Files\Charonum\Wrigley Engine\WE_Startup-main")