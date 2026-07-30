import keyboard
import webbrowser
import sys

slackKey = 'ctrl+alt+s'
stardanceKey = 'ctrl+alt+8'

keyboard.add_hotkey("ctrl+alt+q", lambda: sys.exit())

#websites
keyboard.add_hotkey(slackKey, lambda: webbrowser.open("https://hackclub.enterprise.slack.com/archives/C0APH2MMHH7"))
keyboard.add_hotkey(stardanceKey, lambda: webbrowser.open("https://stardance.hackclub.com/home"))

print("running")
keyboard.wait()