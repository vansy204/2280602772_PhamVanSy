import rsa

class RSACipher:
    def __init__(self):
        (self.pub_key, self.priv_key) = rsa.newkeys(512)

    def encrypt_text(self, text):
        return rsa.encrypt(text.encode(), self.pub_key).hex()

    def decrypt_text(self, cipher_hex):
        cipher_bytes = bytes.fromhex(cipher_hex)
        return rsa.decrypt(cipher_bytes, self.priv_key).decode()