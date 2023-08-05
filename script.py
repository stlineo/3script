import subprocess
import ctypes
import webbrowser

command = ""
while command != "quit":
    command = input("""___________________________________________________________________________________________________
|                                                                                                 |
|   3script by 3xtfs          v0.1-trashver          trash script that i will probably use later  |
|_________________________________________________________________________________________________|
|                                                                                                 |
| Getting Started                                                          _                      |
|                                                                        /\ \                     |
|  [1.] Activation (MAS)                                                /  \ \                    |
|  [2.] ThisisWin11                                                    / /\ \ \                   |
|  [3.] Free wallpapers                                               / / /\ \ \                  |
|                                                                     \/_//_\ \ \                 |
| Applications                                                          __\___ \ \                |
|                                                                      / /\   \ \ \               |
|  [4.] Google Chrome                                                 / /_/____\ \ \              |
|  [5.] Firefox                                                      /__________\ \ \             |
|  [6.] Opera                                                        \_____________\/  3script    |
|  [7.] Opera GX                                                                                  |
|  [8.] Vivaldi                                                                                   |
|  [9.] Maxthon                                                                                   |
|  [10.] ungoogled-chromium                                                                       |
|  [11.] Brave                                                                                    |
|  [12.] Waterfox                                                                                 |
|  [13.] LibreWolf                                                                                |
|  [14.] Internet Finder (by stx4 :3)                                                             |
|                                                                                                 |
|  [15.] 7-zip                                                                                    |
|  [16.] WinRar                                                                                   |
|  [17.] Notepad++                                                                                |
|  [18.] Visual Studio Code                                                                       |
|  [19.] Python                                                                                   |
|                                                                                                 |
|  [20.] Discord Desktop                                                                          |
|                                                                                                 |
| Other                                                                                           |
|  [21.] Classic Photo Viewer                                                                     |
|  [22.] NoWindowsUpdate                                                                          |
|_________________________________________________________________________________________________|
                    
> """).lower()
    if command == "1":
        p = subprocess.Popen(['programs\\GettingStarted\\MAS_AIO.cmd'])
    elif command == "2":
        p = subprocess.Popen(['programs\\GettingStarted\\TIW11\\ThisIsWin11.exe'])
    elif command == "3":
        link = "https://wallhaven.cc/"
        webbrowser.open(link)
    elif command == "4":
        p = subprocess.Popen(['programs\\Applications\\Browsers\\ChromeSetup.exe'])    
    elif command == "5":
        p = subprocess.Popen(['programs\\Applications\\Browsers\\Firefox Installer.exe'])
    elif command == "6":
        p = subprocess.Popen(['programs\\Applications\\Browsers\\OperaSetup.exe'])
    elif command == "7":
        p = subprocess.Popen(['programs\\Applications\\Browsers\\OperaGXSetup.exe'])
    elif command == "8":
        p = subprocess.Popen(['programs\\Applications\\Browsers\\Vivaldi.6.1.3035.257.x64.exe'])
    elif command == "9":
        p = subprocess.Popen(['programs\\Applications\\Browsers\\maxthon_7.0.2.2001_x64.exe'])
    elif command == "10":
        p = subprocess.Popen(['programs\\Applications\\Browsers\\ungoogled-chromium_115.0.5790.99-1.1_installer_x64.exe'])    
    elif command == "11":
        p = subprocess.Popen(['programs\\Applications\\Browsers\\BraveBrowserSetup-BRV010.exe'])
    elif command == "12":
        p = subprocess.Popen(['programs\\Applications\\Browsers\\Install Waterfox.exe'])
    elif command == "13":
        p = subprocess.Popen(['programs\\Applications\\Browsers\\librewolf-116.0-1-windows-x86_64-setup.exe'])
    elif command == "14":
        p = subprocess.Popen(['programs\\Applications\\Browsers\\InternetFinder40Setup.exe'])
    elif command == "15":
        p = subprocess.Popen(['programs\\Applications\\Utilities\\7z2301-x64.exe'])
    elif command == "16":
        p = subprocess.Popen(['programs\\Applications\\Utilities\\winrar-x64-623.exe'])    
    elif command == "17":
        p = subprocess.Popen(['programs\\Applications\\Utilities\\npp.8.5.4.Installer.x64.exe'])
    elif command == "18":
        p = subprocess.Popen(['programs\\Applications\\Utilities\\VSCodeUserSetup-x64-1.81.0.exe'])
    elif command == "19":
        p = subprocess.Popen(['programs\\Applications\\Utilities\\python-3.11.4-amd64.exe'])
    elif command == "20":
        p = subprocess.Popen(['programs\\Applications\\Communication\\DiscordSetup.exe'])
    elif command == "21":
        command = 'reg add "HKLM\Software\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations" /v ".png" /t REG_SZ /d "PhotoViewer.FileAssoc.Tiff" /f'
        subprocess.Popen(command, shell=True)
        ctypes.windll.user32.MessageBoxW(0, "Command Success", "process", 0)
    elif command == "22":
        command = 'sc config wuauserv start=disabled'  
        subprocess.Popen(command, shell=True)
        ctypes.windll.user32.MessageBoxW(0, "Command Success", "process", 0)
    elif command == "quit":
        break
    else:
        ctypes.windll.user32.MessageBoxW(0, "Input isn't a listed option.", "!! Alert !!", 0)
