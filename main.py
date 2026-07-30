import keyboard
import webbrowser
import sys
import subprocess
import os

hackclubKey = 'ctrl+alt+h'
slackKey = 'ctrl+alt+s'
stardanceKey = 'ctrl+alt+8'
lapseKey = 'ctrl+alt+l'


hcLock = False
sysLock = False
hardLock = False

systemKey = 'ctrl+alt+shift+1'
powershellKey = 'ctrl+alt+`'
sysInfoKey = 'ctrl+alt+i'
vscodeKey = 'ctrl+alt+v'
gitBashKey = 'ctrl+alt+b'

hardwareKey = 'ctrl+alt+w'
onshapeKey = 'ctrl+alt+o'
kicadKey = 'ctrl+alt+k'
claudeKey = 'ctrl+alt+c'
# unlocker

def hcunlocker():
    global hcLock, sysLock, hardLock
    hcLock = True
    sysLock = False
    hardLock = False
    webbrowser.open("https://hackclub.com/")
    print("\033[1m" + "Operation Hack Club has been opened!" + "\033[0m")

def sysUnlocker():
    global hcLock, sysLock, hardLock
    sysLock = True
    hcLock = False
    hardLock = False
    subprocess.Popen(["cmd", "/c", "start", "ms-settings:"])
    print("operation system settings opened")

def hardUnlocker():
    global hcLock, sysLock, hardLock
    hcLock = False
    sysLock = False
    hardLock = True
    print("Hardware tools are now open for use!")


# launchers
#hc
def open_slack():
    if hcLock:
        webbrowser.open("https://hackclub.enterprise.slack.com/archives/C0APH2MMHH7")

def open_stardance():
    if hcLock:
        webbrowser.open("https://stardance.hackclub.com/home")

def open_lapse():
    if hcLock:
        webbrowser.open("https://lapse.hackclub.com")
#sys
def open_powershell():
    if sysLock:
        os.system("start powershell")

def open_sys_info():
    if sysLock:
         os.system("start msinfo32")

def openGitBash():
    if not sysLock:
        return
        
    admin_path = r"C:\Program Files\Git\git-bash.exe"
    user_path = os.path.expandvars(r"C:\Users\%USERNAME%\AppData\Local\Programs\Git\git-bash.exe")

    try:
        subprocess.Popen([admin_path])
    except FileNotFoundError:
        try:
            subprocess.Popen([user_path])
        except FileNotFoundError:
            print("❌ Git Bash was not found in standard paths.")

def open_vscode():
    if sysLock:
        os.system("start code")
#hardware
def open_onshape():
    if hardLock:
        webbrowser.open("https://cad.onshape.com/signin")

def open_kicad():
    if hardLock:  # Everything indented inside here so it only triggers when unlocked
        base_dir = r"C:\Program Files\KiCad"
    
        if os.path.exists(base_dir):
            for folder in os.listdir(base_dir):
                exe_path = os.path.join(base_dir, folder, "bin", "kicad.exe")
                if os.path.exists(exe_path):
                    os.system(f'start "" "{exe_path}"')
                    return
                    
        print("❌ KiCad was not found in C:\\Program Files\\KiCad\\")

def open_claude():
    if hardLock:
        webbrowser.open("https://claude.ai/new")


keyboard.add_hotkey("ctrl+alt+q", lambda: sys.exit())

# Activation Hotkeys
keyboard.add_hotkey(hackclubKey, lambda: hcunlocker())
keyboard.add_hotkey(systemKey, lambda: sysUnlocker())
keyboard.add_hotkey(hardwareKey, lambda: hardUnlocker())

# Hack Club Hotkeys
keyboard.add_hotkey(slackKey, open_slack)
keyboard.add_hotkey(stardanceKey, open_stardance)
keyboard.add_hotkey(lapseKey, open_lapse)

# System Hotkeys
keyboard.add_hotkey(powershellKey, open_powershell)
keyboard.add_hotkey(sysInfoKey, open_sys_info)
keyboard.add_hotkey(gitBashKey, openGitBash)
keyboard.add_hotkey(vscodeKey, open_vscode)

# Hardware Hotkeys
keyboard.add_hotkey(kicadKey, open_kicad)
keyboard.add_hotkey(onshapeKey, open_onshape)
keyboard.add_hotkey(claudeKey, open_claude)


filename = "README.md"  # Change to "readme.txt" if your file uses a text extension

if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as file:
        print("\n--- README CONTENT ---")
        print(file.read())
        print("----------------------\n")
else:
    print(f" Notice: {filename} was not found in the script directory.")



print("running")
keyboard.wait()