class TranspositionCipher:
    def __init__(self):
        pass
    def encrypt(self, text, key):
        encrypted_text = ""
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, encrypted_text, key):
        num_rows = len(encrypted_text) // key
        num_extra_chars = len(encrypted_text) % key
        num_long_cols = num_extra_chars  # Số cột có hàng dư
        num_short_cols = key - num_extra_chars  # Số cột ngắn hơn

        decrypted_text = ["" for _ in range(num_rows + 1)]
        index = 0

        for col in range(key):
            row_length = num_rows + 1 if col < num_long_cols else num_rows
            for row in range(row_length):
                decrypted_text[row] += encrypted_text[index]
                index += 1

        return "".join(decrypted_text)