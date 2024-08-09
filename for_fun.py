import pyautogui
import time
import win32gui
import pyperclip  # Clipboard handling

def get_active_window_title():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

while True:
    # Check if the active window is Facebook
    active_window = get_active_window_title()
    if "Facebook" in active_window:  # Adjust this string to match the Facebook window title
        pyperclip.copy("😘")  # Copy emoji to clipboard
        pyautogui.hotkey("ctrl", "v")  # Paste the emoji
        pyautogui.press('enter')  # Press Enter to send
    time.sleep(1)  # Adjust the time (in seconds) as needed
