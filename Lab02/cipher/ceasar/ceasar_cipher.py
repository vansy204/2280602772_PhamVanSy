from cipher.ceasar.alphabet import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.ALPHABET = ALPHABET
    def encrypt_text(self,text:str, key:int) -> str:
        alphabet_len = len(self.ALPHABET)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            letter_index = self.ALPHABET.index(letter)
            output_index = (letter_index + key) % alphabet_len  
            output_letter = self.ALPHABET[output_index]
            encrypted_text.append(output_letter)
        return "".join(encrypted_text)
    def decrypt_text(self,text:str, key:int) -> str:
        alphabet_len = len(self.ALPHABET)
        text = text.upper()
        decrypted_text = []
        for letter in text:
            letter_index = self.ALPHABET.index(letter)
            output_index = (letter_index - key) % alphabet_len  
            output_letter = self.ALPHABET[output_index]
            decrypted_text.append(output_letter)
        return "".join(decrypted_text)
    