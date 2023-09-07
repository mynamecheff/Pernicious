from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os

def generate_salt():
    return os.urandom(16)

def encrypt_file(input_file, output_file, password):
    salt = generate_salt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=1000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    
    with open(input_file, 'rb') as f_input:
        with open(output_file, 'wb') as f_output:
            f_output.write(salt)
            
            encryptor = cipher.encryptor()
            while True:
                chunk = f_input.read(1024)
                if not chunk:
                    break
                encrypted_chunk = encryptor.update(chunk)
                f_output.write(encrypted_chunk)

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "encrypted_output.enc"
    password = "your_password_here"
    
    encrypt_file(input_file, output_file, password)
