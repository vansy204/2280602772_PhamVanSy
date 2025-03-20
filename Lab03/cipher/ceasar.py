class CaesarCipher:
    def encrypt_text(self, text, key):
        result = ''
        for char in text:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                result += chr((ord(char) - offset + key) % 26 + offset)
            else:
                result += char
        return result

    def decrypt_text(self, text, key):
        return self.encrypt_text(text, -key)
