from ecies.utils import generate_key
from ecies import encrypt, decrypt

class ECCCipher:
    def __init__(self):
        self.key = generate_key()
        self.private_key = self.key.to_hex()
        self.public_key = self.key.public_key.format(True).hex()

    def encrypt_text(self, text):
        return encrypt(self.public_key, text.encode()).hex()

    def decrypt_text(self, cipher_hex):
        return decrypt(self.private_key, bytes.fromhex(cipher_hex)).decode()
