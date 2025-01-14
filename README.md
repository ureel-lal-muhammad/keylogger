# Ethical Keylogger with Encryption and Decryption

## Overview

This project is an ethical keylogger designed to capture user keystrokes in real-time, record timestamps for each key press, and securely store the captured data in an encrypted log file. The keylogger operates with Python and employs encryption (Fernet) to ensure the confidentiality of the logged keystrokes.

## Features

- **Keystroke Capture**: Records every key press made by the user.
- **Timestamping**: Logs each keystroke with an accurate timestamp.
- **Buffering**: Optimizes performance by buffering keystrokes before writing them to a file.
- **Encryption**: Captured keystrokes are encrypted using the Fernet encryption system.
- **Decryption**: Decrypt the log files to view the captured keystrokes.
- **Ethical Use**: The keylogger is intended for ethical and legitimate purposes only.

## Components

The project consists of three main files:

1. **keyloggerv2.py**: The core logic for capturing keystrokes and storing them with timestamps.
2. **encryption.py**: Handles the encryption and generation of the encryption key.
3. **decryption.py**: Allows for decryption and viewing of the encrypted log file.

## Keylogger Workflow

1. **Keystroke Capture**: The keylogger listens for key presses, logging each with a timestamp.
2. **Buffering**: Keystrokes are buffered to optimize file writes.
3. **File Encryption**: Once the ESC key is pressed, the captured keystrokes are written to a log file and encrypted using Fernet.
4. **Decryption**: Use the `decryption.py` script to decrypt and view the log file content.

## Setup

1. **Install Dependencies**:
   To run this project, you will need to install the following Python libraries:

   ```bash
   pip install pynput cryptography
